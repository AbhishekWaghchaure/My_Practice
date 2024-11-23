"""Pyramid Pattern
Problem Description:
You are given an integer n. Your task is to return a pyramid pattern of '*' where each side has n rows, represented as a list of strings. The pyramid is centered, with 1 star in the first row, 3 stars in the second row, and so on, increasing by 2 stars per row until the base row has 2n - 1 stars.

Input:
A single integer n, where 1 <= n <= 100.

Output:
A list of strings where each string contains stars ('*') centered, forming a pyramid shape. Each row has an increasing number of stars, with appropriate spaces for centering.

Example:
Input: 3
Output: ['  *  ', ' *** ', '*****']
 
Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']"""

def pyramid(num):
    if num < 1:
        return []
    
    pyramid = []
    for i in range(1,num+1):
        spaces = ' ' * (num - i)
        stars = '*' * (2*i - 1)
        pyramid.append(spaces + stars)
    return(pyramid)
    
print("\n".join(pyramid(10)))
print(pyramid(5))



############################################################################################################################################################################################################################

def pyramid2(num):
    if num < 1:
        retrn = []
        
    total_width = num * 2 - 1
    pyramid = []
    for i in range(1,num+1):
        stars = (2 * i -1) * "*"
        with_spaces = stars.center(total_width)
        pyramid.append(with_spaces)
    return pyramid
    
print(pyramid2(5))
print("\n".join(pyramid2(5)))