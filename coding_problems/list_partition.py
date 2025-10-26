# Partition a list into 2 where the shorter list has higher sum
def partition_list(arr):
    n = len(arr)
    if n < 2:
        return None 
    limit = (n - 1) // 2  # maximum allowed size of first sublist
    a = sorted(arr, reverse=True)
    total = sum(a)
    prefix = 0
    for k in range(1, limit + 1):
        prefix += a[k - 1]
        if prefix > total - prefix:
            first = a[:k]
            second = a[k:]
            return first, second
    return None  # impossible
    
# ✅ and ❌ color codes
GREEN = "\033[92m"  # bright green
RED = "\033[91m"    # bright red
RESET = "\033[0m"

def run_test(name, arr, expected):
    result = partition_list(arr)
    if result == expected:
        print(f"{GREEN}✓ {name} passed{RESET}")
    else:
        print(f"{RED}✗ {name} failed{RESET}")
        print(f"   Input: {arr}")
        print(f"   Expected: {expected}")
        print(f"   Got:      {result}")

if __name__ == "__main__":
    run_test("Test 1", [1, 2, 3, 10], ([10], [3, 2, 1]))  # order after sort
    run_test("Test 2", [1, 2, 3], None)
    run_test("Test 3", [5, 5, 5, 5], None)
    run_test("Test 4", [1, 2, 100, 3, 4], ([100], [5, 4, 3, 2, 1]))
    run_test("Test 5", [10, 20, 30, 40, 50, 60], ([60, 50], [40, 30, 20, 10]))
    run_test("Test 6", [10, 5], None)
    run_test("Test 7", [-1, -2, 10, 5], ([10], [5, -1, -2]))
    run_test("Test 8", [100, 90, 80, 1, 1, 1], ([100, 90], [80, 1, 1, 1]))