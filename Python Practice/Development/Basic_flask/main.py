from flask import Flask, render_template
import requests

"""
it creates an instance to flask class, which will be our (web server gatway interface )application.
"""

## WGGI application
app = Flask(__name__)

# @app.route("/")
# def welcome():
#     return '<html> <h1> Welcome to this best Flask App. build by abhishek </h1></html>'

@app.route('/index', methods = ['GET'])
def welcome_index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/welcome/<name>')
def welcome(name):
    return f'<h1> Hi {name} welcome to this shitty world!! </h1>'

if __name__ == '__main__':
    app.run(debug = True)
