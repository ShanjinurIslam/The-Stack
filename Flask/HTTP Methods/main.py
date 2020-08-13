from flask import Flask,request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return 'Index Page'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET'