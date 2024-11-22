"""Right Angled Triangle
Problem Description:
You are given an integer n. Your task is to return a right-angled triangle pattern of '*' where each side has n characters, represented as a list of strings. The triangle has '*' characters, starting with 1 star in the first row, 2 stars in the second row, and so on until the last row has n stars.

Input Parameters:
n (int): The height and base of the right-angled triangle.

Output:
A list of strings where each string is a row of '*' characters that increases in length from 1 to n.

Example:
Input: 3
Output: ['*', '**', '***']
 
Input: 5
Output: ['*', '**', '***', '****', '*****']
"""

def right_angled_triangle(num):
    pattern = []
    for i in range(1,num+1):
        pattern.append(i * "*")
    return pattern
    
print("\n".join(right_angled_triangle(5)))