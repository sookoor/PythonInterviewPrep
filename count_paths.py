from collections import defaultdict

def _count_paths(x, y, obstacles, memo=None):

    if memo is None:
        memo = defaultdict(int)

    if obstacles is not None and (x, y) in obstacles:
        return 0
    if (x, y) in memo:
        return memo[(x, y)]
    elif x == 0 and y == 0:
        memo[(x, y)] = 1
        return 1
    elif x < 0 or y < 0:
        memo[(x, y)] = 0
        return 0
    
    return _count_paths(x - 1, y, obstacles, memo) + _count_paths(x, y - 1, obstacles, memo)

def count_paths(N, obstacles=None):
    return _count_paths(N - 1, N - 1, obstacles)

if __name__ == "__main__":
    print count_paths(3, [(1, 1)])
