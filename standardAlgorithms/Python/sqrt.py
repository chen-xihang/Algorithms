def sqrt(x):
    """
    Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well. LeetCode #69
    """
    if x <0:
        raise ValueError("Cannot take the square root of a negative number.")
    if x == 0 or x == 1:
        return x
    
    l = 0
    u = x
    while l <= u:
        m = (l+u)//2
        if m*m == x:
            return m
        if m*m < x:
            l = m + 1
        else:
            u = m - 1
    return u 


# Examples
sqrt(6)
sqrt(0)
sqrt(-1)
sqrt(45)



def squareRootWithPrecision(number, precision):
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if number == 0:
        return 0
    if precision < 0:
        raise ValueError("Precision must be a non-negative integer.")
    
    # Step 1: Find the integer part of the square root using binary search
    start, end = 0, number
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == number:
            ans = mid
            break
        if mid * mid < number:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    
    if precision == 0:
        return ans
    
    # Step 2: Find the fractional part up to the specified precision
    for i in range(1, precision+2):
        start = ans
        for _ in range(10):
            while (ans + 10**(-i)) ** 2 <= number:
                ans = ans + 10**(-i)
            else:
                break

    return round(float(ans), precision)
        

# Example usage:
squareRootWithPrecision(-1, 0)  # Output: error
squareRootWithPrecision(3, 0)   # Output: 1
squareRootWithPrecision(3, 1)   # Output: 1.7
squareRootWithPrecision(3, 2)   # Output: 1.73
squareRootWithPrecision(9, 1) #  Output: 3.0