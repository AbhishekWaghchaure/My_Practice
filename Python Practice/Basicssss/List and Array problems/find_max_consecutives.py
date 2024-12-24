"""
Max Consecutive Ones
Asked in Companies:
Google
Amazon
Microsoft
Facebook

Description:
Given a binary array nums, return the maximum number of consecutive 1s in the array.

Input Parameters:
nums (List[int]): A binary array where each element is either 0 or 1.
Output:
int: The maximum number of consecutive 1s in the array.

Example:
Input: nums = [0, 0, 0, 0]
Output: 0

Input: nums = [1, 0, 1, 1, 0, 1, 1, 1, 1]
Output: 4

Input: nums = [1, 1, 0, 1, 1, 1]
Output: 3

Disclaimer: This Udemy coding exercise is still in development, so some advanced complexities might not be fully checked. Please use it primarily for basic code validation.

LeetCode Link: https://leetcode.com/problems/max-consecutive-ones/description/
"""
# def consecutives(nums):
#     count_0 = 0
#     count_1 = 1
#     for i in range(len(nums)-1):
#         if nums[i] == 0:
#             count_0 += 1
#         elif nums[i] == 1:
#             count_1 += 1
#         elif nums[i] != 0 and nums[i] != 1:
#             return f"The element is not zero or one --- invalid list/arrya"
#     if count_0 >= count_1:
#         return 0
#     else:
#         return 1

def consecutives(nums):
    max_count = 0
    current_count = 0
    for i in nums:
        if i == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else :
            current_count = 0
    max_count = max(max_count, current_count)

    return max_count
# nums = [0, 0, 0, 0]
# nums =[1,0,0,1,1,0,0]
nums = [1, 1, 0, 1, 1, 1]
print(consecutives(nums))