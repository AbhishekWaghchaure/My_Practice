number = int(input('Enter then number of digits in an arrya'))

user_list = []
for i in range (number):
    element = int(input(f'Enter the {i+1} element :'))
    user_list.append(element)
    
print(f'User created list is:{user_list}')

max = user_list[0]

for i in range (1,len(user_list)):
    if user_list[i] > max:
        max = user_list[i]
    
    else:
        max = max
print(f'Max Value for this list is:{max}')