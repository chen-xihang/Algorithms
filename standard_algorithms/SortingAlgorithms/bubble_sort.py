"""
Time complexity O(N^2)
"""
def bubbleSort(arr):
    n = len(arr)
    counter = 1
    while counter > 0:
        counter = 0
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                counter += 1
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


# Example usage:
if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubbleSort(sample_array)
    print("Sorted array is:", sorted_array)