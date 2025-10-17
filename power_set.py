def power_set(arr):
    if not arr:
        return [[]]
    x = power_set(arr[:-1])
    y = arr[-1]

    ans = [p + [y] for p in x]

    return x + ans