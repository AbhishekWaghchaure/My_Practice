"""Problem Description:
You are given two integers, n and m. Your task is to return a rectangle pattern of '*', where n represents the number of rows (length) and m represents the number of columns (breadth).

Input:
Two integers n and m, where 1 <= n, m <= 100.

Output:
A list of strings where each string represents a row of the rectangle pattern.

Example:
Input: n = 4, m = 5
Output: ['*****', '*****', '*****', '*****']
 
Input: n = 3, m = 2
Output: ['**', '**', '**']"""

def rectangle_pattern(num1, num2):
    pattern = [num1 * '*']  # 3
    
    for i in range(1, num2): #4
        pattern.append(num1 * '*')
    return pattern

print("\n".join(rectangle_pattern(3,4)))
        