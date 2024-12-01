"""Selection Sort
Selection Sort Algorithm
You are given a list of integers. Write a Python function to sort the list in ascending order using the Selection Sort algorithm. Selection Sort works by repeatedly finding the minimum element from the unsorted part of the list and swapping it with the first element of the unsorted part.
Parameters:
lst (List of integers): The list to be sorted.
Returns:
A list of integers sorted in ascending order.
Example:
Input: lst = [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]
Input: lst = [29, 10, 14, 37, 13]
Output: [10, 13, 14, 29, 37]"""

def selection_sort(arr):
    min = 0
    for i in range(0, len(arr)-1):
        for j in range(i + 1 ,(len(arr))):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
                
    return arr

print(selection_sort([64, 25, 12, 22, 11]))