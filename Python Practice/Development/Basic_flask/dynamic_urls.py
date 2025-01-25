from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return f"<h1> Welcome to homepage </h1>"

## Hard coded URLS without path parameters
@app.route('/welcome/steve')
def welcome_steve():
    return f'<h1>Hey Steve welcome to your personalised page </h1>'

@app.route('/welcome/tony')
def welcome_tony():
    return f'<h1>Hey Tony welcome to your personalised page </h1>'

##Path parameter
@app.route('/welcome/<name>')
def welcome_name(name):
    return f'<h1>Hey {name.title()} welcome to your personalised page </h1>'



if __name__ == '__main__':
    app.run(debug=True)