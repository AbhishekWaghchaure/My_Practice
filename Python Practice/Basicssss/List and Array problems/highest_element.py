"""
Maximum Element in a List.
Asked in Companies:
Google
Amazon
Microsoft
Facebook

Description:
Given a list of integers, write a function to find the maximum element in the list.

Input Parameters:
lst (List[int]): A list of integers.
Output:
int: The maximum element in the list.

"""

def highest_element(lst):
    highest_element = 0
    for i in range(len(lst)):
        if lst[i] > highest_element:
            highest_element = lst[i]
    return highest_element

l = [12,11,45,65,33,23,98,-1,-99]
print(highest_element(l))
