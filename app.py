from flask import Flask,render_template,request,redirect,url_for,session
import mysql.connector as c
import database as db
import app
import pandas as pd
con = c.connect(host = "localhost",user = "root",password = "honeychandu",database = 'project')
cursor = con.cursor()
app = Flask(__name__)
app.secret_key = "irischandu"
@app.route('/signin', methods = ['GET','POST'])
def signin():
    if request.method=='POST':
        email = request.form['email']
        passw = request.form['password']
        data = db.signin(email)
        user = db.name(email)
        session['user'] = user
        signin.custid = db.custidf(email) 
        if passw in data:
            return render_template('home.html',msg=user[0])
    else:
        if "user" in session:
            return render_template('home.html')
        else:
            return render_template('signin.html')
@app.route('/', methods = ['GET'])
def home():
    if "user" in session:
        user = session['user']
        return render_template("home.html",msg=user)
    else:
        return render_template("signin.html")
@app.route('/logout',methods = ['GET','POST'])
def logout():
    session.pop("user", None)
    return render_template("logout.html")

@app.route('/signup',methods = ['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    name   = request.form['fullname']
    email  = request.form['email']
    mobile = request.form['number']
    gender = request.form['gender']
    pass1  = request.form['password1']
    pass2  = request.form['password2']
    data   = db.signup_val()
    if email in data:
        return render_template('signup.html',msg = 'Looks like you are already registered')
    elif pass1 == pass2:
        insert = db.signup(name,email,mobile,gender,pass1)
        return render_template('signup.html',msg = insert)
    else:
        return render_template('signup.html',msg ='Password Miss match')

if __name__ =='__main__':
    app.run(port = 5000,debug = True)
    print("welcome!!!!!!!!")
    