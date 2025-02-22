def binary_search(target: int, arr: list) -> int:
    # it's possible to use L < R and R = m - 1 but it's recommended to use < to avoid off-by one errors
    # R = m - 1 is no longer necessary thus we can proceed to using R = m
    if len(arr) == 0: return -1

    L = 0
    R = len(arr) - 1
    while L < R:
        m = L + (R - L) // 2 # (L + R) // 2
        if arr[m] < target:
            L = m + 1
        elif arr[m] > target:
            R = m
        else:
            return m

    if arr[L] == target: return L

    return -1


def test_binary_search():
    # Test with an existing target
    assert binary_search(3, [1, 2, 3, 4, 5]) == 2, "Test case 1 failed"
    
    # Test with a target that is the first element
    assert binary_search(1, [1, 2, 3, 4, 5]) == 0, "Test case 2 failed"
    
    # Test with a target that is the last element
    assert binary_search(5, [1, 2, 3, 4, 5]) == 4, "Test case 3 failed"
    
    # Test with a target not in the list
    assert binary_search(6, [1, 2, 3, 4, 5]) == -1, "Test case 4 failed"
    
    # Test with an empty list
    assert binary_search(3, []) == -1, "Test case 5 failed"
    
    # Test with a one-element list (element present)
    assert binary_search(3, [3]) == 0, "Test case 6 failed"
    
    # Test with a one-element list (element absent)
    assert binary_search(2, [3]) == -1, "Test case 7 failed"
    
    # Test with a list where target is not in the middle
    assert binary_search(10, [2, 3, 5, 7, 8, 10, 12, 14]) == 5, "Test case 8 failed"
    
    print("All test cases passed!")

# Run the test function
test_binary_search()
