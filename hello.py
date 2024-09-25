from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
# ...
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
# home page
@app.route('/')
def index():
 return render_template('index.html')
# user page
@app.route('/user/<name>')
def user(name):
 return render_template('user.html', name=name, current_time = datetime.utcnow())