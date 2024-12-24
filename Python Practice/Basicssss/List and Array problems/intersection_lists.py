"""
Intersection of two Lists
Asked in Companies:
Google
Amazon
Microsoft
Facebook

Description:
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique, and you may return the result in any order.

Input Parameters:
nums1 (List[int]): An array of integers.
nums2 (List[int]): An array of integers.
Output:
List[int]: An array of unique integers that are present in both nums1 and nums2.

Example:
Input: nums1 = [1, 2, 3], nums2 = [4, 5, 6]
Output: []

Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2]

Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Output: [9, 4]

Disclaimer: This Udemy coding exercise is still in development, so some advanced complexities might not be fully checked. Please use it primarily for basic code validation.

LeetCode Link: https://leetcode.com/problems/intersection-of-two-arrays/

"""
def check_intersection(nums1, nums2):
    intersection = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums2[j] == nums1[i]:
                intersection.append(nums2[j])
    intersection = list(set(intersection))
    return intersection
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(check_intersection(nums1,nums2))