def all_subsets(s):
    num_subsets = pow(2,len(s))
    subset_list = []
    
    for i in range(num_subsets):
        subset = []
        bitmask = i
        index = len(s) - 1
        while bitmask > 0:
            if bitmask & 1:
                subset.append(s[index])
            bitmask >>= 1
            index -= 1
        subset_list.append(subset)
    return subset_list

if __name__ == "__main__":
    print all_subsets([1, 2, 3])
