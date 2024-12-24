"""
Calculator
Create a Python class named Calculator with the following specifications:
Constructor Method (__init__): Initializes two attributes, num1 and num2.
Method add: Takes no arguments and returns the sum of num1 and num2.
Method subtract: Takes no arguments and returns the result of subtracting num2 from num1.
Method multiply: Takes a single argument factor and returns the product of num1 and factor.
Method divide: Takes a single argument divisor and returns the result of dividing num1 by divisor. If divisor is zero, print an error message and return None.
Example:
Creating an instance of the Calculator class
calculator = Calculator(10, 5)

# Testing the add method
print("Addition Result:", calculator.add())  # Output: 15

# Testing the subtract method
print("Subtraction Result:", calculator.subtract())  # Output: 5

# Testing the multiply method
print("Multiplication Result:", calculator.multiply(3))  # Output: 30

# Testing the divide method
print("Division Result:", calculator.divide(2))  # Output: 5.0
print("Division Result:", calculator.divide(0))  # Output: Error: Cannot divide by zero
"""

class Calculator:
    def __init__(self,num_a,num_b):
        self._a = num_a  ## Protected data members
        self._b = num_b

    ## Getter and Setter Functions
    def get_a(self):
        return self._a
    def get_b(self):
        return self._b
    def set_a(self,a):
        self._a = a
    def set_b(self, b):
        self._b = b

    ## Addition
    def add(self):
        return f"{self._a} + {self._b} = {self._a + self._b}"

    ## Subtraction
    def subtract(self):
        return f"{self._a} - {self._b} = {self._a - self._b}"

    ## Multiply
    def multiply(self):
        return f"{self._a} * {self._b} = {self._a * self._b}"

    ## Division
    def division(self):
        return f"{self._a} / {self._b} = {self._a / self._b}"

    ## Modulus
    def mod(self):
        return f"{self._a} % {self._b} = {self._a % self._b}"



print("World Clas Claculator XD --- sarcastic")
a = int(input('Enter the First Number :'))
b = int(input('Enter the Second Number :'))
calculator = Calculator(a,b)
operation = str(input('Enter any Mathematical operation you want to perform : '))

if operation in ('+', 'add', 'addition') :
    print(f"Addition of 2 numbers : {calculator.add()}")

elif operation in ('-', 'sub', 'subtraction') :
    print(f"Subtraction of 2 numbers : {calculator.subtract()}")

elif operation in ('*', 'mul', 'multiply') :
    print(f"Multiply of 2 numbers : {calculator.multiply()}")

elif operation in ('/', 'div', 'division') :
    print(f"Division of 2 numbers : {calculator.division()}")

elif operation in ('%', 'mod', 'modulus') :
    print(f"Modulus of 2 numbers : {calculator.mod()}")

else:
    raise TypeError()


