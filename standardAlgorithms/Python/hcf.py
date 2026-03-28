def euclideanAlgorithm(a, b):
    """Compute the highest common factor (HCF) of two integers using the Euclidean algorithm.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The highest common factor of a and b.
    """
    a = max(a,b)
    b = min(a,b)

    while b > 0:
        a, b = b, a%b
    return a
    
# example usage
euclideanAlgorithm(48, 18)