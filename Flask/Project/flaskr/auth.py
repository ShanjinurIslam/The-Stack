import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from werkzeug.security import check_password_hash, generate_password_hash
from .db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        error = None
        
        if not username:
            error = 'Username is required'
            return render_template('auth/register.html',error=error)
        elif not password:
            error = 'Password is required.'
        elif db.execute('SELECT id FROM user WHERE username = ?', (username,)).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)
            return render_template('auth/register.html',error=error)
        
        if error is None:
            db.execute(
            'INSERT INTO user (username, password) VALUES (?, ?)',
            (username, generate_password_hash(password)) )

            db.commit()
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html')

@bp.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        username = request.form['username'] 
        password = request.form['password'] 
        
        db = get_db()
        
        error = None
        user = db.execute('SELECT * FROM user WHERE username = ?', (username,) ).fetchone()
        
        if user is None:
            error = 'Incorrect username.'
            return render_template('auth/login.html',error = error)
        elif not check_password_hash(user['password'], password): 
            error = 'Incorrect password.'
            return render_template('auth/login.html',error = error)
        if error is None: 
            session.clear()
            session['user_id'] = user['id']
            session['user_name'] = user['username']
            return redirect(url_for('index'))

    return render_template('auth/login.html')


@bp.route('/logout', methods=['POST']) 
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
