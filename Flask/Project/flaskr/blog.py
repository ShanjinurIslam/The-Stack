import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, abort

from werkzeug.security import check_password_hash, generate_password_hash
from .db import get_db

bp = Blueprint('blog', __name__, url_prefix='/')


@bp.route('/')
def index():
    if session:
        db_instance = get_db()
        posts = db_instance.execute(
            'SELECT p.id, title, body, created, author_id, username FROM post p JOIN user u ON p.author_id = u.id ORDER BY created DESC').fetchall()

        return render_template('index.html', posts=posts)
    else:
        return redirect(url_for('auth.login'))


@bp.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        authod_id = request.form['authod_id']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)' ' VALUES (?, ?, ?)',
                (title, body, authod_id)
            )
            db.commit()
            flash(f"{title} Added", category="success")
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


@bp.route('/view/<int:post_id>', methods=['GET'])
def view_post(post_id):
    db = get_db()
    post = db.execute(
        'SELECT p.id, title, body, created, author_id, username FROM post p JOIN user u ON p.author_id = u.id WHERE p.id = ?',
        (post_id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(post_id))

    return render_template('blog/view.html', post=post)


@bp.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        if not title:
            error = 'Title is required.'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?' ' WHERE id = ?', (title, body, post_id))
            db.commit()
            return redirect(f'/view/{post_id}')

    db = get_db()
    post = db.execute(
        'SELECT p.id, title, body, created, author_id, username FROM post p JOIN user u ON p.author_id = u.id WHERE p.id = ?',
        (post_id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(post_id))

    return render_template('blog/update.html', post=post)

@bp.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    db = get_db()
    db.execute(
        'DELETE FROM post WHERE id = ?', (post_id,))
    db.commit()
    flash('Post deleted',category="danger")
    return redirect(url_for('blog.index'))
            