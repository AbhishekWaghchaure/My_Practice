from flask import Flask,redirect,url_for,render_template
from employee import emp

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html', title = 'HomePage')

@app.route('/about')
def about():
    return render_template('about.html', title = 'AbOuTPaGe')

@app.route('/main/<name>')
def main(name):
    return f'<h1> Hello!!! {name.title()}. </h1>'

@app.route('/pass/<sname>/<int:marks>')
def passed(sname, marks):
    return f'<h1> Congtats {sname} have passed with {marks} marks!! </h1>'

@app.route('/fail/<sname>/<int:marks>')
def fail(sname, marks):
    return f'<h1> Sorry {sname} have failed with {marks} marks!! </h1>'

@app.route('/score/<name>/<int:num>')
def score(name, num):
    if num > 60:
        return redirect(url_for('passed', sname = name, marks = num))
    else:
        return redirect(url_for('fail', sname = name, marks = num))
    
@app.route('/evaluate/<int:num>')
def evaluate(num):
    return render_template('evaluate.html', title = 'Evaluate',
                           number = num)
    
@app.route('/employee')
def employee():
    return render_template('employee.html', title = 'Employee', employee = emp)

@app.route('/employee/managers')
def managers():
    return render_template('manager.html', title = 'Managers', employee = emp)

if __name__ == '__main__':
    app.run(debug = True)