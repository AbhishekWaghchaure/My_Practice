"""
Rotate List
Asked in Companies:
Google
Amazon
Microsoft
Facebook

Description:
Given a list of integers and an integer D, write a function to rotate the list to the left by D positions.

Input Parameters:
ARR (List[int]): A list of integers.
D (int): The number of positions to rotate the list to the left.
Output:
List[int]: The list after rotating it to the left by D positions.

Example:
Input: ARR = [1, 2, 3, 4, 5], D = 2
Output: [3, 4, 5, 1, 2]

Input: ARR = [10, 20, 30, 40, 50], D = 3
Output: [40, 50, 10, 20, 30]

Input: ARR = [7, 8, 9, 10], D = 1
Output: [8, 9, 10, 7]
"""

## Wrong
def rotate_left_loop(lst,idx):
    left = 0
    right = idx

    if 0 < idx < len(lst):
        while left <= right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        return lst
    else:
        return f"The {idx} index is not within range of length of array"

array = [1,2,3,4,5,6]
rotator = 3
print(rotate_left_loop(array, rotator))

## corrected
#1st function to rotate all elements
def reverse(arr, start, end):
    start = start
    end = end

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

## 2nd function to correct the rotations
def rotate_left_inplace(ARR, D):
    if len(ARR) == 0 or D == 0:
        return ARR

    D = D % len(ARR)

    reverse(ARR, start = 0, end =(len(ARR)-1))

    reverse(ARR, start = 0, end = len(ARR) - D - 1)

    reverse(ARR, start = len(ARR) - D, end = len(ARR)-1)

    return ARR

## Using slicing
def rotate_left_slicing(arr, d):
    if len(arr) == 0 or d ==0:
        return arr
    d = d % len(arr)

    return arr[d:] + arr[:d]

l = [1,2,3,4,5,6]
print(rotate_left_inplace(l, 3))
# print(rotate_left_slicing(l, 3))
