# num = 20
# USER DEFINED CODE
num = int(input("Enter the number you want to check if it is prime or not"))
count = 0
if num > 1:
    for i in range(1,num+1):
        if (num % i == 0):
            count += 1
if count == 2:
    print("The number you entered IS a Prime number")
else:
 print("The number you entered is NOT Prime number")