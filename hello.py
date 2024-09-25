from flask import Flask
app = Flask(__name__)
# home page
@app.route('/')
def index():
 return '<h1>Hello World!</h1>'
# user page with name of user
@app.route('/user/<name>')
def user(name):
 return '<h1>Hello, {}!</h1>'.format(name)