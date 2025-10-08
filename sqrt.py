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