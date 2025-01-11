from flask import Flask, redirect, url_for
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> Welcome To The Homepage !!</h1>"

@app.route('/score/<name>/<int:num>')
def score(name, num):
    if num > 30:
        time.sleep(1)
        #redirect to page pass
        return redirect(url_for('passed'))
    else:
        time.sleep(1)
        ## redirect to page Fail
        return redirect(url_for('fail'))
    
@app.route('/pass')
def passed():
    return f"<h1> Congrats you have passed!! </h1>"

@app.route('/fail')
def fail():
    return f"<h1> Sorry, you have failed!! </h1>"

if __name__ == '__main__':
    app.run(debug = True)