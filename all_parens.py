def _all_parens(cur_str, num, paren_set):
    if len(cur_str) == num * 2:
        paren_set.add(cur_str)
    else:
        for i in range(len(cur_str)):
            _all_parens("(" + cur_str[0:i] + ")" + cur_str[i:], num, paren_set)

def all_parens(num):
    paren_set = set()
    _all_parens("()", num, paren_set)
    return list(paren_set)

if __name__ == "__main__":
    print all_parens(3)
