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



def is_palindrome(string):
    start = 0
    end = len(string) - 1

    while True:
        if start > end:  # Stop condition when pointers cross
            break
        if string[start] != string[end]:  # Compare characters
            return False
        start += 1  # Move start forward
        end -= 1    # Move end backward

    return True

# Test case
print(is_palindrome("abcdedcba"))  # Output: True
print(is_palindrome("abccbaaa"))  # Output: False


def is_palindrom_for(string):
    start  = 0
    end = len(string) - 1
    
    for i in range(len(string) // 2):
        if string[start] != start[end]:
            return False
        
        start += 1
        end -= 1