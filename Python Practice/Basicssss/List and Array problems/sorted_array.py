"""
Is Array Sorted?
Asked in Companies:
Google
Microsoft
Amazon
Facebook

Description:
Write a function that checks whether the given array is sorted in non-decreasing order. The array is considered sorted if every element is less than or equal to the next element.

Input Parameters:
arr (List[int]): A list of integers.
Output:
bool: True if the array is sorted in non-decreasing order, False otherwise.

Example:
Input: arr = [5, 4, 3, 2, 1]
Output: False

Input: arr = [1, 3, 2, 4, 5]
Output: False

Input: arr = [1, 2, 3, 4, 5]
Output: True

Disclaimer: This Udemy coding exercise is still in development, so some advanced complexities might not be fully checked. Please use it primarily for basic code validation.

Leetcode Link : No Direct link is available.

"""
def sorted_check(arr):
    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            return False
    return True

# lst = [5,4,3,2,1]
lst= [1,3,2,4,5]
# lst=[1,2,3,4,5]
print(sorted_check(lst))