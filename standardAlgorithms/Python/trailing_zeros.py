"""
Given an integer n, return the number of trailing zeroes in n!.
LeetCode #172.
"""
def trailingZeroes(self, n):
    ans = 0
    for i in range(n):
        if n // (5 ** (i + 1)) == 0:
            break
        ans += n // (5 ** (i + 1))
    return ans


# Example usage:
print(trailingZeroes(100))  # Output: 24:
print(trailingZeroes(25))   # Output: 6
print(trailingZeroes(5))    # Output: 1
print(trailingZeroes(0))    # Output: 0
        