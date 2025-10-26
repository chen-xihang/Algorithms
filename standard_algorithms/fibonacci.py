# using DP

def fibonacci(n, a=1, b=1):
    if n == 1:
        return a
    if n == 2:
        return b
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
