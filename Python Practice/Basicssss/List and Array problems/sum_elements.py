"""
Sum of Elements in a List
Asked in Companies:
Google
Amazon
Microsoft
Facebook

Description:
Given a list of integers, write a function to find the sum of all the elements in the list.

Input Parameters:
lst (List[int]): A list of integers.
Output:
int: The sum of all the elements in the list.

"""
def sum_list(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum

lst = [11,-2,-4,8,10,12]
print(sum_list(lst))