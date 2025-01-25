from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

## Entity class
class EmployeeModel(db.Model):
    # __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable =False, unique = True)
    department = db.Column(db.String(50), nullable = False)
    salary = db.Column(db.Integer, nullable = False)

    # def __repr__(self):
    #     return f"Employee('{self.name}')"

## Traditional Employee class
class Employee:
    def __init__(self, id, name, age, email,department, salary):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.department = department
        self.salary = salary

    def save_to_db(self):
        try:
            if not self.id:
                new_employee = EmployeeModel(name=self.name, department=self.department, salary=self.salary)
                db.session.add(new_employee)
                db.session.commit()
                self.id = new_employee.id
            else:
                employee = EmployeeModel.query.get(self.id)
                if employee:
                    employee.name = self.name
                    employee.department = self.department
                    employee.salary = self.salary
                    db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def to_dic(self):
        return{
            'id' : self.id,
            'name' : self.name,
            'age' : self.age,
            'email' : self.email,
            'department' : self.department,
            'salary' : self.salary
        }
    @staticmethod
    def get_all_employees():
        employees = EmployeeModel.query.all()
        return [Employee(e.name, e.age, e.email, e.department, e.salary, e.id).to_dic() for e in employees]

    @staticmethod
    def get_employee_by_id(id):
        e = EmployeeModel.query.get(id)
        if e:
            return Employee(e.name, e.age, e.email, e.department, e.salary, e.id).to_dic()

    @staticmethod
    def delete_employee(id):
        e = EmployeeModel.querry.get(id)
        if e:
            db.session.delete(e)
            db.session.commit()
            return True
        return False

    ##Flash Routes
with app.app_context():
    db.create_all()

@app.route('/employees', methods = ['GET'])
def get_employees():
    return jsonify(Employee.get_all_employees())

@app.route('/employees/<int:id>', methods = ['GET'])
def get_employee(id):
    employee = Employee.get_employee_by_id(id)
    if not employee:
        return jsonify({'message' : 'Employee not found'}), 404
    return jsonify(employee)

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    new_employee = Employee(name = data['name'], age = data['age'], email = data['email'], department = data['department'], salary = data['salary'], id = data['id'])
    new_employee.save_to_db()
    return jsonify({'message':'Employee added successfully!!', 'employee' : new_employee.to_dic()}), 201

if __name__ == '__main__':
    app.run(debug = True)