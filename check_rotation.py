def check_rotation(s1, s2):
    """Assuming method isSubstring checks is one word is a substring of
    another, given two strings, s1 and s2, checks if s2 is a rotation of
    s1 using only one call to isSubstring"""
    s1_len = len(s1)

    if s1_len > 0 and s1_len = len(s2):
        return isSubstring(''.join([s1, s1]), s2)
    return False

if __name__ == "__main__":
    assert check_rotation('apple', 'pleap') == True
    assert check_rotation('apple', 'ppale') == False
    assert check_rotation('waterbottle', 'erbottlewat') == True
