def non_three_repeat_strings(A, B):
    # Implement your solution here
    res = []
    while A>B>0:
        res.append("aab")
        A = A-2
        B = B-1
    while B>A>0:
        res.append("bba")
        A = A-1
        B = B-2
    if A == B and A == 0:
        return "".join(res)
    if A == B:
        for _ in range(A):
            res.append("ab")
        return "".join(res)
    for _ in range(A):
        res.append("a")
    for _ in range(B):
        res.append("b")
    return "".join(res)
    
# Example usage:
non_three_repeat_strings(5, 3)
non_three_repeat_strings(4, 1)