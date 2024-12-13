num = int(input("Enter the number of digits you want in the list"))
lst = []

for i in range(num):
    lst.append(int(input(f"Enter the digit at {i} :")))

print(f"The custom list created is : {lst}")


first = lst[int(input("Enter the first index of an element you want to swap"))-1]
second = lst[int(input("Enter the second index of an element you want to swap "))-1]

# Approach 1 swapping using temp variable
# temp = lst[first]
# lst[first] = lst[second]
# lst[second] = temp

# Approach 2 Direct initialization
# lst[first],lst[second] = lst[second],lst[first]

# Approach 3 pop
first_element = lst.pop(first)
second_element = lst.pop(second-1)

lst.insert(second, first_element)
lst.insert(first, second_element)


#Approach 4 Tuple
print(f"The list after swapping the list elements is :{lst}")