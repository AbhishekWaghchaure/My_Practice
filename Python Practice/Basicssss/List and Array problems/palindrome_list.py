"""
Palindrome List
Asked in Companies:
Google
Amazon
Microsoft
Facebook

Description:
Given a list of integers, determine if it is a palindrome. A list is considered a palindrome if it reads the same forward and backward.

Input Parameters:
lst (List[int]): A list of integers.
Output:
bool: Return True if the list is a palindrome, otherwise False.

Example:
Input: lst = [7, 8, 9, 8, 7]
Output: True

Input: lst = [1, 2, 3, 4, 5]
Output: False

Input: lst = [1, 2, 3, 2, 1]
Output: True
"""

def palindrome_list_direct(lst):
    if lst == lst[::-1]:
        return True
    else:
        return False

lis = [10,23,12,12,23,10]
print(palindrome_list_direct(lis))

################################################################################################################################

def palindrom_list_2pointer(lst):
    start = 0
    end = len(lst) - 1
    while start <= end:
        if lst[start] != lst[end]:
            return False
        start += 1
        end -= 1
    return True

print(palindrom_list_2pointer(lis))
