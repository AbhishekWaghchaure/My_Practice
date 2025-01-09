def insertion_sort(arr):
    length = len(arr)
    for i in range(1,length):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1]  = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


l = [12, 25, 11, 34, 90, 22]
print(insertion_sort(l))
