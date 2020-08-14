from flask import Flask,request,render_template,make_response

app = Flask(__name__)

@app.errorhandler(404) 
def not_found(error):
    response = make_response(render_template('error.html'), 404)
    return response

### Construct APIs

@app.route('/api/get_user_details')
def get_user_details():
    user = {}
    user['name'] = "Shanjinur"
    user['token'] = "SecureText"

    return user,200

