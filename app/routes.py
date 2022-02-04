from app import app 

@app.route('/')
def index():
    return "Hello World"

@app.route('/name')
def name():
    return "Hello Allison"