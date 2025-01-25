from flask import Flask, url_for, redirect, render_template
from forms import SignupForm, LoginForm

app = Flask(__name__)
## CSRF cross site request forgery
app.config['SECRET_KEY'] = 'this is a secret key'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/signup', methods = ['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('signup.html', title = 'Signup', form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)

if __name__ == "__main__":
    app.run(debug = True)
