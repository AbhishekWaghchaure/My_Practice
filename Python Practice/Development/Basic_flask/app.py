from flask import Flask

app = Flask(__name__)

@app.route('/') ### Creation of endpoint
@app.route('/home')
def home():
    return '<h1> Welcome to my home page! </h1>'

@app.route('/about')
def about():
    return '<h1> This is the about page. </h1>'

@app.route('/welcome/<name>')
def welcome(name):
    return f'<h1> Hi {name.title()} welcome to this shitty world!! </h1>'

@app.route('/addition/<int:num>')
def addition(num):
    return f'<h1>Input : {num} ---- Output : {num + 10} </h1>'

@app.route('/addition_2/<int:num1>/<int:num2>')
def addition_2(num1, num2):
    return f'<h1>Input : {num1} + {num2} ---- {num1 + num2} </h1>'

if __name__ == '__main__':
    app.run(debug = True)
    

