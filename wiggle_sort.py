# Sort input list to have the following property: x1 <= x2 >= x3 <= x4 >= ...

def _swap(input_list, i, j):
    input_list[i], input_list[j] = input_list[j], input_list[i]

def wiggle_sort(input_list):
    for i in range(len(input_list) - 1):
        if i % 2 == 0:
            if input_list[i] > input_list[i + 1]:
                _swap(input_list, i, i + 1)
        elif input_list[i] < input_list [i + 1]:
            _swap(input_list, i, i + 1)

    return input_list

if __name__ == "__main__":
    l = [1, 5, 2, 3, 6, 7, 2, 8]
    print(l)
    print(wiggle_sort(l))
