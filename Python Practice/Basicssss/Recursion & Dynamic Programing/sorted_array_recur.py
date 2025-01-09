def sorted_array_recur(arr):
    if(len(arr) == 0 or len(arr) == 1):
        return True
    
    if arr[0] < arr[1]:
        return sorted_array_recur(arr[1:])
    else:
        return False
    
ls = [1,2,3,4,5]
print(sorted_array_recur(ls))