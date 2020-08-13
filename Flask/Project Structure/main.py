from flask import Flask, url_for, request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    # print(url_for('static', filename='style.css'))
    if request.method == 'GET':
        return render_template('index.html', name="Spondon")

