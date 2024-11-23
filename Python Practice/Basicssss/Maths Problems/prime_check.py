"""Check for Prime Number
Problem Description:
You are given an integer n. Your task is to check whether the number is prime or not. A prime number is a number greater than 1 that has no divisors other than 1 and itself. Return True if the number is prime, and False otherwise.

Input:
A single integer n where 1 <= n <= 10^6.

Output:
Return True if n is a prime number, otherwise return False.

Example:
Input: n = 5
Output: True
 
Input: n = 4
Output: False"""

def prime_check(num):
    counter = 0
    if num == 0:
        return False
    if num == 1:
        return False
    if num == 2:
        return True
    
    # if num > 1:
    #     for i in range(num):
    #         if i % num == 0:
    #             counter += 1
    #     if counter == 2:
    #         return True
    #     else:
    #         return False
    
    if num % 2 == 0:
        False
        
    for i in range(3, int(num ** 0.5 + 1), 2):  ## Checking it till underoot of num for efficiency
        if num % i == 0:
            True
        
print(prime_check(2))
        
        