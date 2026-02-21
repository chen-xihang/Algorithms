def maxArray(array):
    if len(array) == 0:
        return None
    else:
        max_val = array[0]
        for num in array[1:]:
            if num >=max_val:
                max_val = num
        
        return max_val
    

## use case
maxArray([1,2,42,3,52,4])
