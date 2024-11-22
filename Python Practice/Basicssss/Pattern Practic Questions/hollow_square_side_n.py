"""Hollow Square of side 'N'
Problem Description:
You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).

Input Parameters:
n (int): The size of the square (number of rows and columns).

Output:
A list of strings where each string is a row of n characters, representing a hollow square.

Example:
Input: 3
Output: ['***', '* *', '***']

Input: 5
Output: ['*****', '*   *', '*   *', '*   *', '*****']"""

def generate_hollow_square(num):

    if num == 1:
        return [num * '*']

    if num == 2:
        return [num * '*', num * '*']
    
    ## first row
    pattern = [num * "*"]

    ## middle rows
    for _ in range(num - 2):
        pattern.append('*' + ' ' * (num - 2) + '*')

    ## Last rows
    pattern.append(num * '*')

    return pattern

# number = int(input("Enter the number for creating hollow pattern : "))
number = 5
print(generate_hollow_square(5))
print("\n".join(generate_hollow_square(3)))  
print("\n".join(generate_hollow_square(5))) 
