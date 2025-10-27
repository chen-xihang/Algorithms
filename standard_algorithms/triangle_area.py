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


def minimal_perimeter(arr):
    """
    Finds the minimum perimeter of any triangle that can be formed
    from three positive integers in arr satisfying the triangle inequality.

    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    y = [x for x in arr if x > 0]
    y.sort()
    n = len(y)
    if n < 3:
        return -1
    found = False
    for i in range(n-2):
        if y[i]+y[i+1]>y[i+2]:
            found = True
            min_n = i
            break
    if not found:
        return -1
    for j in range(min_n+1):
        if y[j] + y[min_n+1] > y[min_n+2]:
            perimeter = y[j] + y[min_n+1] +y[min_n+2]
            break
    
    return perimeter if found else -1

minimal_perimeter([1,2,3,4,5,10])  # Example usage

def empty_triangle_robust(X, Y):
    """
    Finds a triangle with vertices from the given points (X[i], Y[i])
    such that no other points lie inside the triangle.

    Time complexity: O(n^4)
    Space complexity: O(1)
    """
    n = len(X)
    if n < 3:
        return []
    if n == 3:
        x1, y1 = X[0], Y[0]
        x2, y2 = X[1], Y[1]
        x3, y3 = X[2], Y[2]
        if triangle_area([x1, y1], [x2, y2], [x3, y3])==0:
            return []
        return [0, 1, 2]
    
    points = sorted(
        [(X[i], Y[i], i) for i in range(n)],
        key = lambda t: (t[0], t[1])
    )

    for i in range(n-2):
        x1 = points[i][0]
        y1 = points[i][1]
        for j in range(i+1, n-1):
            x2 = points[j][0]
            y2 = points[j][1]
            for k in range(j+1, n):
                x3 = points[k][0]
                y3 = points[k][1]
                if triangle_area([x1, y1], [x2, y2], [x3, y3]) == 0:
                    continue
                empty = True
                for l in range(i+1, k):
                    lx = points[l][0]
                    ly = points[l][1]
                    if point_in_triangle([lx,ly], [x1, y1], [x2, y2], [x3, y3]):
                        empty = False
                        break
                if empty:
                    return [points[i][2], points[j][2], points[k][2]]
    return []
                
                    
import math

def orient(a, b, c):
    (x1, y1), (x2, y2), (x3, y3) = a, b, c
    return (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)

def empty_triangle(X, Y):
    """
    Finds any triangle (p, q, r) formed by the points (X, Y)
    such that no other point lies inside it.
    Returns indices [i, j, k] or [] if no such triangle exists.
    """
    n = len(X)
    if n < 3:
        return []

    pts = [(X[i], Y[i]) for i in range(n)]

    # For each point as pivot
    for i in range(n):
        px, py = pts[i]
        others = []

        # Build list of other points with angle and squared distance
        for j in range(n):
            if j == i:
                continue
            dx = pts[j][0] - px
            dy = pts[j][1] - py
            ang = math.atan2(dy, dx)
            if ang < 0:  # normalize angle to [0, 2π)
                ang += 2 * math.pi
            dist2 = dx*dx + dy*dy
            others.append((ang, dist2, j))

        if len(others) < 2:
            continue

        # Sort by angle (then distance on same ray)
        others.sort(key=lambda t: (t[0], t[1]))

        m = len(others)
        # Check consecutive pairs in circular order
        for k in range(m):
            _, _, j1 = others[k]
            _, _, j2 = others[(k + 1) % m]

            # Skip collinear cases (no area)
            if orient((px, py), pts[j1], pts[j2]) == 0:
                continue

            # Found a valid empty triangle
            return [i, j1, j2]

    return []

