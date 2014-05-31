def _compress_intervals(intervals):
    if len(intervals) == 1:
        return intervals
    else:
        cur = intervals[0]
        rest = _compress_intervals(intervals[1:])
        if cur[1] >= rest[0][0] and cur[1] < rest[0][1]:
            if cur[0] < rest[0][0]:
                rest[0][0] = cur[0]
        else:
            rest.insert(0, cur)
        return rest
            
            
def is_covered(l, q):
    sorted_intervals = sorted(l, key=lambda item: item[1])
    compressed_intervals = _compress_intervals(sorted_intervals)
    if compressed_intervals is not None:
        for interval in compressed_intervals:
            if q[0] >= interval[0] and q[1] < interval[1]:
                return True
    return False


if __name__ == "__main__":
    l = [[1, 6], [3, 5], [7, 9]]
    q1 = (2, 4)
    q2 = (5, 7)
    assert is_covered(l, q1) == True
    assert is_covered(l, q2) == False
