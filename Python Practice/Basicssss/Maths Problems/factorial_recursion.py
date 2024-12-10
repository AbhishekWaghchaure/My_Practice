"""Factorial of a number using Recursion
Problem Description:
You are given a non-negative integer n. Your task is to find the factorial of n, defined as the product of all positive integers less than or equal to n. The factorial of 0 is defined to be 1. You must implement this using recursion.

Input:
A non-negative integer n, where 0 <= n <= 20.

Output:
An integer representing the factorial of n.

Example:
Input: n = 5
Output: 120

Input: n = 0
Output: 1
"""

def factorial_recursion(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial_recursion(num - 1)

print(factorial_recursion(5))

def factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = i * factorial
    return factorial

print(factorial(10))
