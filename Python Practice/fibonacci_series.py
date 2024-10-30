3
num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))

print (num1)
print(num2)

for i in range(2,10):
    sum = num1 + num2
    print(sum)
    num1 = num2
    num2 = sum