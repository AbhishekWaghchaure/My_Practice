number = int(input('Enter the number of digits you want in the list :'))

user_list = []
for i in range (number):
    user_list.append(int(input(f"Enter the number at {i+1} :")))
    print(f'User generated list is : {user_list}')
    
## Code to find the min of list

min = user_list[0]

for i in range(number):
    if user_list[i] < min:
        min = user_list[i]
    else :
        min = min
print(min)