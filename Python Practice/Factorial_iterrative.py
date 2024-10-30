factorial = 1
num = int(input("Enter the value of number whose factorial we want to count"))

if num < 0:
    print("Factorial does not exist for negative numbers")
elif (num == 0):
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("Factorial of this number is ", factorial)