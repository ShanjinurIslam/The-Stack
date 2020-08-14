from flask import Flask,request,render_template,make_response

app = Flask(__name__)

# set cookie

@app.route('/') 
def index():
    resp = make_response(render_template('index.htm')) 
    resp.set_cookie('username', 'Spondon') 
    return resp

@app.route('/username') 
def get_username():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a 
    # KeyError if the cookie is missing.
    if username:
        return username,200
    else:
        return "Not Found",404

