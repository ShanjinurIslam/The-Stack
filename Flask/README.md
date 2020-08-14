# Flask

## Installation

### Install Flask Binaries

```
pip install Flask
```

### Create an environment

```
python -m venv venv
. venv/bin/activate
```

### Install ```virtualenv``` 

```
sudo python -m pip install virtualenv
```

## Run Application

```
export FLASK_APP=main.py
flask run
```

### Turn on ```debug mode``` 

 If you enable debug support the server will reload itself on code changes, and it will also provide you with a helpful debugger if things go wrong.

```
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

~~~~{.python}
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
~~~~


## HTTP Methods

~~~~{.python}

@app.route('/',methods=['GET'])
def index():
    return 'Index Page'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET'

~~~~

## Template Rendering

Inside of ```render_template()``` function we can provide multiple argument, for suppose here ```name``` argument is provided

~~~~{.python}

@app.route('/',methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html', name="Spondon")

~~~~

And to use this argument inside ```index.html```

~~~~{.html}

<body>
{% if name %}
    <h1>Hello {{ name }}!</h1> 
{% else %}
    <h1>Hello, World!</h1> 
{% endif %}
</body>

~~~~







