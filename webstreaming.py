
from flask import render_template, redirect, url_for, request
import flask

app = flask.Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/index')
def index():
    return render_template('index.html')
        
@app.route('/other')
def other():
    return render_template("other.html")
    
    
@app.route('/live')
def live():
    return render_template("live.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

if __name__== "__main__":
    app.run(port=8080)
