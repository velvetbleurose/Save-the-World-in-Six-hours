from flask import Flask
from flask import Flask, Response, request, render_template, redirect, url_for
import flask
#from flaskext.mysql import MySQL
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'user'
app.config['MYSQL_DATAHBASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABSE_DB'] = 'dbname'
app.config['MYSQL_DATABASE_HOST'] = 'host'

@app.route("/login",methods=['GET','POST'])
def login():
    if flask.request.method == 'GET':
        return render_template('login.html')
    elif flask.request.method == 'POST':
        return render_template('home.html', register='True')

@app.route("/",methods=['GET'])
def hello():
    return render_template('home.html', register='False')
    
@app.route("/user",methods=['GET'])
def user():
    return render_template('user.html')

@app.route("/register",methods=['GET','POST'])
def register():
    if flask.request.method == 'GET':
        return render_template('regsiter.html')
    elif flask.request.method == 'POST':
        return
if __name__ == "__main__":
    app.run(port='5000')
