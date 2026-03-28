def quickSort(arr):
    def partion(l,r):
        if l >= r:
            return
        p = l
        pivot = arr[r]
        for i in range(l,r):
            if arr[i] < pivot:
                arr[i], arr[p] = arr[p], arr[i]
                p += 1
            if arr[i] >= pivot:
                arr[i], arr[r] = arr[r], arr[i]
            
        partion(l, p-1)
        partion(p+1, r)

    partion(0, len(arr)-1)

    return arr


# test case

x = [4,2,4,3,1,4,1,10,3,2,0]

print(quickSort(x))
