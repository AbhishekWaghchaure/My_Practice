"""
Fibonacci Series using Recursion
Problem Description:
You are given a non-negative integer n. Your task is to find the nth Fibonacci number using recursion. The Fibonacci sequence is defined as follows:
F(0)=0F(0) = 0F(0)=0
F(1)=1F(1) = 1F(1)=1
For n≥2n \geq 2n≥2, F(n)=F(n−1)+F(n−2)F(n) = F(n-1) + F(n-2)F(n)=F(n−1)+F(n−2)

Input:
A non-negative integer n, where 0 <= n <= 30.

Output:
An integer representing the nth Fibonacci number.

Example:
Input: n = 5
Output: 5  # Fibonacci sequence: 0, 1, 1, 2, 3, 5

Input: n = 0
Output: 0  # F(0) = 0

"""

def fibonacci_recur(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1

    # return fibonacci_recur(num - 1) + fibonacci_recur(num - 2)
    last = fibonacci_recur(num - 1)
    second_last = fibonacci_recur(num - 2)
    return last + second_last

print(fibonacci_recur(5))

