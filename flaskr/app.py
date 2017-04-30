from flask import Flask
from flask import Flask, Response, request, render_template, redirect, url_for
import flask
#from flaskext.mysql import MySQL
import mongoQ
import flask.ext.login as flask_login

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'savetheworld'
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/savetheworld'

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

mongo = mongoQ.stwishDB(app)

@login_manager.user_loader
def user_loader(username):
    uid = mongo.getUID({"username":username})
    if uid == None:
        return
    user = User()
    user.id = username
    return user

@login_manager.request_loader
def request_loader(request):
    uid = mongo.getUID({"username":request.form.get("username"),"password":request.form.get("password")})
    if uid == None:
        return
    user = User()
    user.id = request.form.get("username")
    user.is_authenticated = True
    return user

@app.route("/login",methods=['GET','POST'])
def login():
    if flask.request.method == 'GET':
        return render_template('login.html')
    elif flask.request.method == 'POST':
        #get username account info
        uid = mongo.getUID({"username":request.form.get("username")})
        #errorcheck if username exists
        if uid == None:
            return render_template('login.html', message='Username not found')
        #error check if username/password pair is correct
        #TODO: security
        uid = mongo.getUID({"username":request.form.get("username"),"password":requests.get.form("password")})
        if uid == None:
            return render_template('login.html', message='Incorrect username/password')
        
        return render_template('home.html')
@app.route("/",methods=['GET'])
def hello():
    return render_template('home.html', register='False')
    
@app.route("/user",methods=['GET','POST'])
def user():
    if flask.request.method == 'GET':
        return render_template('user.html', changedVal='False')
    elif flask.request.method =='POST':
        #db stuff
        return render_template('user.html', changedVal='True')
    
@app.route("/register",methods=['GET','POST'])
def register():
    if flask.request.method == 'GET':
        return render_template('register.html')
    elif flask.request.method == 'POST':
        username = requests.form.get("username")
        password = requests.form.get("password")
        #error check if username already exists within the system.
        uid = mongo.getUID({"username":request.form.get("username")})
        if uid == None:
            return render_template('register.html', message = 'Username already taken')
        #else create account
        mongo.createAccount({'username':username,'password':password})
        return render_template('home.html', register='True')
if __name__ == "__main__":
    app.run(port='5000')
