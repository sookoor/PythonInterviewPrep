# An O(long(n)) algorithm that finds an element in a increasingly
# sorted array of n integers that has been rotated an unknown number
# of times. 

def _search_rotated(array, left, right, val):

    if left > right:
        return None

    mid = left + ((right - left) // 2)
    
    if array[mid] == val:
        return mid

    # If left half is in increasing order
    elif array[left] < array[mid]:
        if array[left] <= val and val < array[mid]:
            right = mid - 1
        else:
            left = mid + 1

    # Right half is in increasing order
    elif array[left] > array[mid]:
        if array[mid] < val and array[right] >= val:
            left = mid + 1
        else:
            right = mid - 1

    # Skip duplicate value
    else:
        left += 1

    return _search_rotated(array, left, right, val)

def search_rotated(array, val):
    return _search_rotated(array, 0, len(array) - 1, val)

if __name__ == "__main__":
    input_array = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    assert search_rotated(input_array, 5) == 8
    assert search_rotated(input_array, 2) is None
    
    input_array = [3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25, 1]
    assert search_rotated(input_array, 3) == 0
    assert search_rotated(input_array, 21) is None

    input_array = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25]
    assert search_rotated(input_array, 5) == 3
    assert search_rotated(input_array, 22) is None

    assert search_rotated([], 5) is None
