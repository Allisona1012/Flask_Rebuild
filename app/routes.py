from app import app 
from flask import render_template
from app.forms import RegistrationForm

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
        print ("Form has been validated")

    return render_template('register.html', form = form ) 