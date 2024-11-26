"""Check Palindrome
Problem Description:
You are given a string s. Your task is to check if the string is a palindrome. A string is considered a palindrome if it reads the same forward and backward, ignoring spaces, punctuation, and case.

Input:
A single string s, where the length of s is between 1 and 1000.

Output:
A boolean value: True if the string is a palindrome, and False otherwise.

Example:
Input: "A man a plan a canal Panama"
Output: True
 
Input: "Hello, World!"
Output: False"""

def palindrome(string):
    str = "".join(char.lower() for char in string if char.isalnum())
    if str == str [::-1]:
        return True
    else:
        return False
print(palindrome('malayalam'))