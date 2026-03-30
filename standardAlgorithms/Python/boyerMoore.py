def boyerMoore(arr):
    counter = 0
    candidate = None
    
    for s in arr:
        if counter == 0:
            candidate = s
            counter += 1
        elif s == candidate:
            counter += 1
        else:
            counter -= 1
    
    return candidate

