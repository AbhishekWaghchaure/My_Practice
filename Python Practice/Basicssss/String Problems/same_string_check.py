"""Check for same strings
Problem Description:
You are given two strings s and t. Your task is to check if the two strings are equal. Two strings are considered equal if they have the same length and the same characters at each position. You are not allowed to use any built-in string comparison functions.

Input:
Two strings s and t, where 1 <= len(s), len(t) <= 1000.

Output:
A boolean value (True or False) indicating whether the two strings are equal.

Example:
Input: s = "hello", t = "hello"
Output: True
 
Input: s = "hello", t = "world"
Output: False
"""

def similarity_check(string1, string2):
    if len(string1) != len(string2):
        return False
    
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False
    return True
print(similarity_check("abhi","jayy"))
print(similarity_check("abhi","abhi"))
print(similarity_check("abhi","jay"))