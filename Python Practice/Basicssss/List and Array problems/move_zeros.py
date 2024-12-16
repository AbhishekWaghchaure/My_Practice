"""
Move Zeroes
Asked in Companies:
Google
Amazon
Microsoft
Facebook

Description:
Given an integer array nums, write a function to move all 0s to the end of the array while maintaining the relative order of the non-zero elements.

Input Parameters:
nums (List[int]): A list of integers.
Output:
The list nums with all 0s moved to the end, preserving the order of non-zero elements.

Example:
Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

Input: nums = [0, 0, 1]
Output: [1, 0, 0]

Input: nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
Output: [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]

https://leetcode.com/problems/move-zeroes/description/
"""

def move_zeros(arr):
    non_zero = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[non_zero] = arr[non_zero], arr[i]
            non_zero = non_zero + 1
    return arr

lst = [10,30,0,20,12,0,45]
print(move_zeros(lst))