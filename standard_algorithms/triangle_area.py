def triangle_area(A, B, C):
    """
    Calculate the area of a triangle given its vertices A, B, and C.

    Parameters:
    A, B, C: Tuples or lists representing the (x, y) coordinates of the triangle's vertices.

    Returns:
    The area of the triangle.
    """
    x1, y1 = A[0], A[1]
    x2, y2 = B[0], B[1]
    x3, y3 = C[0], C[1]

    area = (1/2)*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))

    return area

triangle_area([0,0], [4,0], [0,3])  # Example usage
triangle_area((1,2), (3,4), (5,0))  # Another example usage