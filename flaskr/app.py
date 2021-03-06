from flask import Flask
from flask import Flask, Response, request, render_template, redirect, url_for
import flask
import mongoQ
import flask_login
import send


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'savetheworld'
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/savetheworld'
app.secret_key="deadsea"

mongo = mongoQ.stwishDB(app)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(username):
    uid = mongo.getUID({"username":username})
    if uid == None:
        return
    user = User()
    user.id = username
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
        uid = mongo.getUID({"username":request.form.get("username"),"password":request.form.get("password")})
        if uid == None:
            return render_template('login.html', message='Incorrect username/password')
        
        user = User()
        user.id = request.form.get("username")
        flask_login.login_user(user)
        return render_template('home.html')
    
@app.route("/",methods=['GET', 'POST'])
def hello():
    if flask.request.method =="GET":
        return render_template('home.html', register='False')
    elif flask.request.method == 'POST':
        print("Hello")
        username = request.form.get("username")
        print("Hello")
        password = request.form.get("password")
        #error check if username already exists within the system.
        print("Hello")
        uid = mongo.getUID({"username":request.form.get("username")})
        print("Hello")
        if uid != None:
            print("Bye")
            return render_template('home.html', message = 'Username already taken')
        #else create account
        print("HelloLast")
        uid = mongo.createAccount({'username':username,'password':password, 'fullname':request.form.get('fullname')})
        mongo.createAccInfo({'uid':uid['uid'], "contacts": [{"name":request.form.get("name"), "phone":request.form.get("phone")}]})
        return render_template('home.html', register='True')

@app.route("/user",methods=['GET','POST'])
@flask_login.login_required
def user():
    if flask.request.method == 'GET':
        return render_template('user.html', changedVal='False')
    elif flask.request.method =='POST':
        #db stuff

        mongo.addInput({'uid':mongo.getUID({'username':flask_login.current_user.id})['uid'], 'mood': request.form.get("mood"), 'feel':request.form.get('feel'), 'appetite':request.form.get('appetite'), 'productivity':request.form.get('motivation'), 'sleep':request.form.get('sleep'), 'energy':request.form.get('energy'), 'social':request.form.get('social'), 'goals':request.form.get('goals')})

        send.check_date(mongo,{'uid':mongo.getUID({'username':flask_login.current_user.id})['uid']})



        return render_template('user.html', changedVal='True')
    
@app.route("/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return redirect(url_for('/'))

if __name__ == "__main__":
    app.run(port='5000')
