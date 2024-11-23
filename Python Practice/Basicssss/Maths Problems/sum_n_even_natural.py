"""Sum of N Even Natural Numbers
Problem Description:
You are given an integer n. Your task is to calculate and return the sum of the first n even natural numbers. The even natural numbers are: 2, 4, 6, 8, ...

Input:
A single integer n where 1 <= n <= 10^4.

Output:
Return the sum of the first n even natural numbers.

Example:
Input: n = 3
Output: 12  # (2 + 4 + 6)
 
Input: n = 5
Output: 30  # (2 + 4 + 6 + 8 + 10)
"""

def sum(num):
    sum = 0
    if 1 <= num <= 10 ** 4:
        for i in range(1, num + 1):
            sum += 2 * i
        return sum

print(sum(10))