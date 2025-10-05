import math
# Returns True if x is prime, else False
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# Sieve of Eratosthenes to count number of primes <= n
def count_primes(n):
    x = [True]*(n+1)
    x[0] = x[1] = False
    for p in range(2, int(n**0.5) + 1):
        x[p*p:n+1:p] = [False]*len(x[p*p:n+1:p])
    return sum(x)

# Sieve of Eratosthenes to list all primes <= n, Segmented
def count_primes_segmented(n):
    if n < 2:
        return 0

    limit = int(math.sqrt(n)) + 1
    # Small primes up to sqrt(n)
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if prime[p]:
            for multiple in range(p*p, limit + 1, p):
                prime[multiple] = False
    primes = [p for p, is_prime in enumerate(prime) if is_prime]

    # Now process in segments
    count = 0
    low = 2
    high = limit # slicing up to width of limit
    while low <= n:
        high = min(high, n + 1)
        mark = [True] * (high - low)
        for p in primes:
            start = max(p*p, (low + p - 1)//p * p) # starting with maximum of p^2 and lowest multiple of p > low
            for j in range(start, high, p):
                mark[j - low] = False
        count += sum(mark)
        low += limit
        high += limit
    return count