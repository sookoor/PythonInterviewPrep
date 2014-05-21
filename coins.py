def _coins(options, n):
    if n == 0:
        return 1
    elif n > 0:
        count = 0
        for i in range(len(options)):
            cur_count = _coins(options[i:], n - options[i])
            if cur_count:
                count += cur_count
        return count

def coins(n):
    return _coins([25, 10, 5, 1], n)

if __name__ == "__main__":
    n = [30, 10, 5, 0, -1]
    for i in n:
        print i
        print coins(i)
        print '---'
