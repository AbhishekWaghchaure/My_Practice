digits = int(input("Enter the digits you want to enter in the list"))

user_list = []
for i in range (digits):
    user_list.append(int(input(f"Enter the {i + 1} element :")))
print(f"User created list is {user_list}")

## to check the length of the user defined list
count = 0
# for i in user_list:
#     count = count + 1
# print(f"The length of the user defined list is {count}")

# for i in range(user_list):
#     count += 1
# print(f'The length of the user defined list is {count}')


## Using Len function

print(f"Using len function {len(user_list)}")