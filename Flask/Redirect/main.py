from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

flag = True

@app.route('/')
def index():
    if flag:
        return redirect(url_for('home'))

    return render_template('index.htm')

@app.route('/home')
def home():
    return "Redirected to home"