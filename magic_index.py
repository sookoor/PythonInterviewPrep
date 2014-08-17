# Given a sorted array, returns an index i if A[i] == i. Returns None
# if no such magic index exists. Assumes array uses 0-based indexing
# so 0 is the first possible magic index if A[0] == 0.

def _magic_index(A, lower, upper):

    i = lower + ((upper - lower) // 2)

    if lower == upper and i != A[i]:
        return None
    elif i == A[i]:
        return i
    elif i < A[i]:
        upper = i
    else:
        lower = i + 1
    return _magic_index(A, lower, upper)

def _magic_index_with_duplicates(A, lower, upper):
    i = lower + ((upper - lower) // 2)

    if lower == upper and i != A[i]:
        return None
    elif i == A[i]:
        return i
    elif i < A[i]:
        left = _magic_index_with_duplicates(A, lower, i)
        if left is None:
            return _magic_index_with_duplicates(A, i + 1, upper)
        else:
            return left
    else:
        right = _magic_index_with_duplicates(A, i + 1, upper)
        if right is None:
            return _magic_index_with_duplicates(A, lower, i)
        else:
            return right

def magic_index(A, duplicates=False):
    if A is not None and len(A) > 0:

        if duplicates is True:
            return _magic_index_with_duplicates(A, 0, len(A) - 1)
        else:
            return _magic_index(A, 0, len(A) - 1)

if __name__ == "__main__":
    assert magic_index([1, 2, 3, 4, 5]) is None
    assert magic_index([0, 1, 2, 3, 4]) == 2
    assert magic_index([0, 1, 3, 4, 5]) == 1
    assert magic_index([-1, 0, 1, 2, 4]) == 4
    assert magic_index([]) is None
    assert magic_index(None) is None

    assert magic_index([1, 2, 3, 3, 4, 5]) is None
    assert magic_index([1, 2, 3, 3, 4, 5], True) == 4
    assert magic_index([0, 0, 1, 4, 5, 6], True) == 0
    assert magic_index([1, 2, 3, 4, 5], True) is None
