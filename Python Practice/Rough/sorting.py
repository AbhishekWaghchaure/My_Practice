## Bubble Sort
def bubble_sort(arr):
    length = len(arr)

    for i in range(length):
        for j in range(0, length - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

array = [10,30,20,29,9,15]
print(bubble_sort(array))


## Selection Sort

def selection_sort(arr):
    length = len(arr)

    for i in range(0, length):
        min = i
        for j in range(i+1, length):
            if arr[j] < arr[min]:
                min = j
        arr[i] , arr[min] = arr[min], arr[i]
    return arr


array = [10,30,20,29,9,15]
print(selection_sort(array))



## Insertion sort

def insertion_sort(arr):
    len = len(arr)
    
    for i in range(0, len):
        sorted = arr[0]
        for j in range(1, len):
            if arr[j] < arr[sorted]:
                sorted = arr[j]
                j = j - 1
                