def array_sum_recur(arr):
    if len(arr) == 0:
        return True
    
    sum = arr[0] + array_sum_recur(arr[1:])
    
    return sum

