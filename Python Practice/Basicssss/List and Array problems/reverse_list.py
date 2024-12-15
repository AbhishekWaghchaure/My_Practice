"""
Reverse a List
Asked in Companies:
Google
Amazon
Microsoft
Apple

Description:
Given a list of integers, write a function to reverse the order of elements in the list.

Input Parameters:
lst (List[int]): A list of integers.
Output:
List[int]: The list with elements in reversed order.

Example:
Input: lst = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Input: lst = [10, 20, 30]
Output: [30, 20, 10]

Input: lst = [7, 8, 9]
Output: [9, 8, 7]

"""
## Using Loop
def reverse_loop(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

## Using Slicing
def reverse_slice(lst):
    return lst[::-1]

## Using reverse function
def reverse_function(lst):
    lst.reverse()
    return lst

l = [1,2,3,4,5,6]
print(reverse_function(l))
