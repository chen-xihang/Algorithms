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

def point_in_triangle(P, A, B, C):
    """
    Determine if point P is inside the triangle formed by vertices A, B, and C.

    Parameters:
    P: Tuple or list representing the (x, y) coordinates of the point to check.
    A, B, C: Tuples or lists representing the (x, y) coordinates of the triangle's vertices.

    Returns:
    True if point P is inside the triangle, False otherwise.
    """
    area_ABC = triangle_area(A, B, C)
    area_PAB = triangle_area(P, A, B)
    area_PBC = triangle_area(P, B, C)
    area_PCA = triangle_area(P, C, A)

    return area_ABC == area_PAB + area_PBC + area_PCA