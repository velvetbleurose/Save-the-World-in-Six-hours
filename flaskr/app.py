from flask import Flask
from flask import Flask, Response, request, render_template, redirect, url_for
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'user'
app.config['MYSQL_DATAHBASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABSE_DB'] = 'dbname'
app.config['MYSQL_DATABASE_HOST'] = 'host'

@app.route("/",methods=['GET'])
def login():
    if flask.request.method == 'GET':
        return render_template('login.html')

@app.route("/",methods=['GET'])
def hello():
    return render_template('home.html')
    
@app.route("/",methods=['GET'])
def user():
    return render_template('user.html')

if __name__ == "__main__":
    app.run(port='5000')
