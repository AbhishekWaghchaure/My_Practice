"""
Missing Number
Asked in Companies:
Google
Microsoft
Amazon
Facebook

Description:
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Input Parameters:
nums (List[int]): A list of integers where each integer is unique and in the range [0, n].
Output:
int: The missing number in the range [0, n].

Example:
Input: nums = [3, 0, 1]
Output: 2

Input: nums = [0, 1]
Output: 2

Input: nums = [8, 7, 6, 4, 3, 2, 0, 1]
Output: 5

Disclaimer: This Udemy coding exercise is still in development, so some advanced complexities might not be fully checked. Please use it primarily for basic code validation.

Leetcode Link : https://leetcode.com/problems/missing-number/description/

"""

def missing_element(arr):
    n = len(arr)
    total_sum = n * (n + 1) // 2
    array_sum = sum(arr)
    # for i in range(n):
    #    array_sum = array_sum + i
    return total_sum - array_sum

lst = [3, 0, 1]
print(missing_element(lst))

