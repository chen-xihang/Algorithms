def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left_result = mergeSort(left)
    right_result = mergeSort(right)

    l1, l2 = 0, 0

    result = []
    while l1 < len(left_result) and l2 < len(right_result):
        if left_result[l1] <= right_result[l2]:
            result.append(left_result[l1])
            l1 += 1
        else:
            result.append(right_result[l2])
            l2 += 1

    result.extend(left_result[l1:])
    result.extend(right_result[l2:])

    return result


# Testing
print(mergeSort([1,4,1,2,42,1,2]))