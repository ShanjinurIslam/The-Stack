from flask import Flask
from maskupsafe import escape

app = Flask(__name__)

## unique routes

@app.route('/projects/') # this is a decorator, A reference to a function "func" or a class "C" is passed to a decorator and the decorator returns a modified function or class
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


## dynamic routes

# (default) accepts any text without a slash
@app.route('/user/<username>')
def show_username(username):
    # show the user profile for that user
    return "Username " % escape(username)


# accepts positive integers
@app.route('/post/<int:post_id>') 
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

# similar types : float, path, uuid
