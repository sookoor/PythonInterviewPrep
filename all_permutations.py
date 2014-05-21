def _swap(input_list, a, b):
    input_list[a], input_list[b] = input_list[b], input_list[a]

def _all_permutations(input_list, pos):
    if pos >= len(input_list):
        print ''.join(input_list)

    for i in range(pos, len(input_list)):
        _swap(input_list, i, pos)
        _all_permutations(input_list, pos + 1)
        _swap(input_list, i, pos)

def all_permutations(input_str):
    _all_permutations(list(input_str), 0)


if __name__ == "__main__":
    input_str = "abc"
    all_permutations(input_str)
