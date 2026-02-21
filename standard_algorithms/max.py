def maxArray(array):
    if len(array) == 0:
        return None
    else:
        max = array[0]
        for num in array[1:]:
            if num >=max:
                max = num
        
        return max
    

## use case
maxArray([1,2,42,3,52,4])
