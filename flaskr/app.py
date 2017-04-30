from flask import Flask
from flask import Flask, Response, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/",methods=['GET'])
def login():
    if flask.request.method == 'GET':
        return render_template('login.html')

@app.route("/",methods=['GET'])
def hello():
    return render_template('home.html')
    

if __name__ == "__main__":
    app.run(port='5000')