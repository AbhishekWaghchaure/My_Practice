"""
Sum of N numbers using Recursion
Problem Description:
You are given a non-negative integer n. Your task is to find the sum of the first n natural numbers using recursion.
The sum of the first n natural numbers is given by the formula S=1+2+3+...+nS = 1 + 2 + 3 + ... + nS=1+2+3+...+n.

Input:
A non-negative integer n, where 0 <= n <= 1000.

Output:
An integer representing the sum of the first n natural numbers.
"""
## Recursion makes use of PMI Principle Of Mathematical Induction
def sum_n_numbers_recur(num):
    if num == 0:  ## Base Cases
        return 0
    elif num == 1:
        return 1
    else:
        return num + sum_n_numbers_recur(num-1) ## Inductive hypothesis true for all k and then inductive step that true for all k - 1


print(sum_n_numbers_recur(5))
