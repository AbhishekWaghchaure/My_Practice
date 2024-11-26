"""Reverse a string
Problem Description:
You are given a string s. Your task is to return the reversed version of the string.

Input:
A single string s, where the length of s is between 1 and 1000.

Output:
A single string that is the reverse of the input string.

Example:
Input: "hello"
Output: "olleh"
 
Input: "Python"
Output: "nohtyP"""

def reverse(string):
    return string[::-1]

print(reverse("Abhishek").lower())