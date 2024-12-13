"""
Number of Digits using Recursion
Problem Description:
You are given a positive integer n. Your task is to find the number of digits in the integer using recursion.

Input:
A positive integer n, where 1 <= n <= 10^9.

Output:
An integer representing the number of digits in n.

Example:
Input: n = 12345
Output: 5

Input: n = 7
Output: 1
"""

def number_of_digits(num):
    if num == 0:
        return 1
    elif 1 <= num <= 9:
        return 1

    return 1 + number_of_digits(num//10)

print(number_of_digits(123459))