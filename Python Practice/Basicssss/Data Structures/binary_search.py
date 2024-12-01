## Array should be sorted for binary search

def binary_search(array, target):
    start = 0   
    end = len(array) - 1
    for _ in range(len(array)):
        mid = start + (end - start) // 2
     
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            end = mid - 1
            
        else:
            start = mid + 1
        
        if start > end:
            break
    return -1



arr = [10,23,32,45,50,67,77,89,98]
target = 67
print(binary_search(arr,target))
