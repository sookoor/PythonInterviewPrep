def remove_dup(string):
    ans_str = string[0]

    for s in string:
        if ans_str.find(s) == -1:
            ans_str += s

    return ans_str

print remove_dup("aabbacc")
