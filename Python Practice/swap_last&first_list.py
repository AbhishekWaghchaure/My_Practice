digit = int(input("Enter the digit of length of list"))

cust_list = []
for i in range(digit):
    cust_list.append(int(input(f"Enter the {i+1} element")))
print(f"The custo list created is {cust_list}")

## Traditional by using a swap variable :

# swap = cust_list[0]
# cust_list[0] = cust_list[len(cust_list) - 1]
# cust_list[len(cust_list) - 1] = swap

# Approach 2
# cust_list[0],cust_list[-1] = cust_list[-1],cust_list[0]

#Approach 3

get = (cust_list[-1],cust_list[0]) # packing 
cust_list[0],cust_list[-1] = get  # unpacking

print(f"The list after swapping : {cust_list}")