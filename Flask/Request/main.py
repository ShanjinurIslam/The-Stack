from flask import Flask,request,render_template

app = Flask(__name__)

def validate_login(username,password):
    return True

@app.route('/',methods=['GET','POST'])
def login_user(username=None):
    return render_template('index.htm',username=username)

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if validate_login(request.form['username'],request.form['password']): # access x-www-form-urlencoded
            return login_user(request.form['username'])
        else:
            error = 'Invalid User'

    return render_template('login.htm',error=error)


@app.route('/upload',methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['profile_picture'] 
        f.save('uploads/'+ f.filename) # file is saved inside /uploads directory
        return "Upload complete",201 # Here 201 is status code of response
        