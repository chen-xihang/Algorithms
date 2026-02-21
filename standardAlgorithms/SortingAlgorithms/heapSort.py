import heapq
# Complexity O(nlog(n))

def heapSort(arr):
    if len(arr) == 1:
        return arr
    heapq.heapify(arr)
    n = len(arr)
    sorted_arr = [0]*n
    for i in range(n):
        sorted_arr[i] = heapq.heappop(arr)
    return sorted_arr
     
# Test cases
heapSort([1,3,5,2,5,1,5,2,4,52,3])