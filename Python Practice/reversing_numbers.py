# num1 = 10
# num2 = 20
# For User defined
num1 = input("Enter the value of number 1 :")
num2 = input("Enter the value of number 2 :23")

print("Number 1 before swapping", num1)
print("Number 2 before swapping", num2)
 
# Approach 1 using temp variable
# temp = num1
# num1 = num2
# num2 = temp

# Approach 2
num1,num2 = num2, num1
 
print("Number 1 after swapping", num1)
print("Number 2 after swapping", num2)