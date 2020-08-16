# Flask

## Installation

### Install Flask Binaries

```bash
pip install Flask
```

### Create an environment

```bash
python -m venv venv
. venv/bin/activate
```

### Install ```virtualenv``` 

```bash
sudo python -m pip install virtualenv
```

## Run Application

```bash
export FLASK_APP=main.py
flask run
```

### Turn on ```debug mode``` 

 If you enable debug support the server will reload itself on code changes, and it will also provide you with a helpful debugger if things go wrong.

```bash
export FLASK_ENV=development
flask run
```

This does the following things:
1. it activates the debugger
2. it activates the automatic reloader
3. it enables the debug mode on the Flask application.

## Project Structure 

```
/application.py 
/templates
    /index.html
/static
    /style.css
```

## Framework Basics

## Routing

Use the ```route()``` decorator to bind a function to a URL.

```python
@app.route('/')
def index():
    return 'Index Page'
```

### Unique routes

```python
@app.route('/projects/') # this is a decorator, A reference to a function "func" or a class "C" is passed to a decorator and the decorator returns a modified function or class
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```


### Dynamic routes

```python
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
```


## HTTP Methods

```python

@app.route('/',methods=['GET'])
def index():
    return 'Index Page'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET'
```

## Template Rendering

Inside of ```render_template()``` function we can provide multiple argument, for suppose here ```name``` argument is provided

```python

@app.route('/',methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html', name="Spondon")

```

And to use this argument inside ```index.html```

```html

<body>
{% if name %}
    <h1>Hello {{ name }}!</h1> 
{% else %}
    <h1>Hello, World!</h1> 
{% endif %}
</body>

```

## Request

### Access Form Data

To access form data (data transmitted in a ```POST``` or ```PUT``` request) you can use the ```form``` attribute. 

```python
@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if validate_login(request.form['username'],request.form['password']): # x-www-form-urlencoded
            return login_user(request.form['username'])
        else:
            error = 'Invalid User'

    return render_template('login.htm',error=error)
```

```application/x-www-form-urlencoded``` - Represents an URL encoded form. This is the default value if ```enctype``` attribute is not set to anything.

### Upload File

You can handle uploaded files with Flask easily. Just make sure not to forget to set the ```enctype="multipart/ form-data"``` attribute on your HTML form, otherwise the browser will not transmit your files at all.

```python
@app.route('/upload',methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['profile_picture'] 
        f.save('uploads/'+ f.filename) # file is saved inside /uploads directory
        return "Upload complete",201 # Here 201 is status code of response
```

## Cookies

To access cookies you can use the ```cookies``` attribute. To set cookies you can use the ```set_cookie``` method of response objects. The ```cookies``` attribute of request objects is a ```dictionary``` with all the cookies the client transmits. If you want to use sessions, do not use the cookies directly but instead use the ```Sessions``` in Flask that add some security on top of cookies for you.

### Set Cookie

```python
from flask import make_response

@app.route('/') 
def index():
    resp = make_response(render_template('index.htm')) 
    resp.set_cookie('username', 'the username') 
    return resp
```

### Access Cookie
```python
@app.route('/username') 
def get_username():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a 
    # KeyError if the cookie is missing.
    if username:
        return username,200
    else:
        return "Not Found",404
```

## Responses

The return value from a view function is automatically converted into a response object for you. If the return value is a string it’s converted into a response object with the string as response body, a ```200 OK``` status code and a ```text/html``` mimetype. If the return value is a dict, ```jsonify()``` is called to produce a response. The logic that Flask applies to converting return values into response objects is as follows:

1. If a response object of the correct type is returned it’s directly returned from the view.
2. If it’s a string, a response object is created with that data and the default parameters.
3. If it’s a dict, a response object is created using jsonify.

### Error Handling

```python
@app.errorhandler(404) 
def not_found(error):
    return render_template('error.html'), 404
```

### Constructing API

```
@app.route('/api/get_user_details')
def get_user_details():
    user = {}
    user['name'] = "Shanjinur"
    user['token'] = "SecureText"

    return user,200

```

As the object is ```dict``` flask will automatically convert it into ```json``` response.

## Redirects

To redirect a user to another endpoint, use the ```redirect()``` function

```python
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
```

## Sessions

In addition to the request object there is also a second object called ```session``` which allows you to store information specific to a user from one request to the next. This is implemented on top of cookies for you and signs the cookies cryptographically. What this means is that the user could look at the contents of your cookie but not modify it, unless they know the secret key used for signing.

### Set the secret key to ```app``` object

```python
from flask import session

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
```

### Add values to session object

```python
session['username'] = request.form['username'] 
```

### Check session value

```python
if 'username' in session:
    return 'Logged in as %s' % escape(session['username'])
```

### Remove session value

```python
session.pop('username', None) 
```

## Blueprints

A ```Blueprint``` is a way to organize a group of related views and other code. Rather than registering views and other code directly with an application, they are registered with a blueprint. Then the blueprint is registered with the application when it is available in the factory function.

### Create instance of ```bp```
```python
from flask import Blueprint
bp = Blueprint('auth', __name__, url_prefix='/auth')
```

### Register with ```app```

```python
app.register_blueprint(auth.bp)
```

### Add route to ```bp```

```python
@bp.route('/logout', methods=['POST']) 
def logout():
    session.pop('user_id',None)
    session.pop('username', None) 
    session.clear()
    return redirect(url_for('auth.login'))
```

## Templates

Templates are files that contain static data as well as placeholders for dynamic data. A template is rendered with specific data to produce a final document. Flask uses the ```Jinja``` template library to render templates.

```app``` will use templates to render ```HTML``` which will display in the user’s browser. In Flask, ```Jinja``` is configured to autoescape any data that is rendered in HTML templates. This means that it’s safe to render user input; any characters they’ve entered that could mess with the HTML, such as < and > will be escaped with safe values that look the same in the browser but don’t cause unwanted effects.

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
    {% block title %}
    {% endblock title %}
    </title>
    <link rel="stylesheet" href="/static/style.css">
</head>

<body>
    {% block navbar %}
        
    {% endblock navbar %}

    {% block content %}
        
    {% endblock content %}
</body>

</html>

```
