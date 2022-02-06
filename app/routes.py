from app import app
from flask import render_template, redirect, url_for
from flask_login import login_user
from app.forms import RegistrationForm, LoginForm
from app.models import User


@app.route('/') #this is part of the url 
def index():#this is a functoin that will run when we go to said web page
    return render_template('index.html') #this pulls the template that will show up on said webpage

@app.route('/name')
def name():
    return render_template('name.html')

@app.route('/register', methods =['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print ("FORM HAS BEEN VALIDATED!")
        #get the data from the form 
        username = form.username.data
        email= form.email.data
        password=form.password.data

        #check to see if username or email is in db
        user_exists = User.query.filter((User.username == username ) | (User.email == email)).all()
        if user_exists:
            return redirect(url_for('Register'))

        #create a new User
        User(username=username, email = email, password= password)
        return redirect(url_for('index'))
    return render_template('register.html', form = form ) 

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #grab data from the form 
        username = form.username.data
        password = form.password.data
        # Query user table for user with username 
        user = User.query.filter_by(usermname = username).first()
        # if the user does not exist or the user has an incorrect password 
        if not user or user.check_password(password):
            #redirect to login page
            return redirect(url_for('login'))

        #if the user does exist 
        login_user(user)
        return redirect(url_for('index'))
        
    return render_template('login.html', form =form )