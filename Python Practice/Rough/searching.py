
def linear_search(arr, target):
    length = len(arr)
    for i in range(length):
        if arr[i] == target:
            return i
    return -1


array = [2,4,3,1,6,9]
print(linear_search(array, 3))


## Binary Search

def binary_search(arr, target):
    length = len(arr)
    start = 0
    end = length - 1
    for i in range(length):
        mid = end - start

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            end = mid - 1

        else:
            start = end + 1
    return -1
array2 = [10,22,36,39,40,59]
print(binary_search(array2, 39))