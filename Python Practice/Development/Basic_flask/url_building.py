from flask import Flask, redirect, url_for
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> Welcome To The Homepage !!</h1>"

@app.route('/pass/<sname>/<int:marks>')
def passed(sname, marks):
    return f"<h1> Congrats {sname} you have passed with {marks} marks!! </h1>"

@app.route('/fail/<sname>/<int:marks>')
def fail(sname, marks):
    return f"<h1> Sorry {sname}, you have failed with {marks} marks!! </h1>"

@app.route('/score/<name>/<int:num>')
def score(name, num):
    if num > 30:
        time.sleep(1)
        #redirect to page pass
        return redirect(url_for('passed', sname = name, marks = num))
    else:
        time.sleep(1)
        ## redirect to page Fail
        return redirect(url_for('fail', sname = name, marks = num))

if __name__ == '__main__':
    app.run(debug = True)