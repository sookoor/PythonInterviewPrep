# An algorithm that determines if a string has all unique characters
def unique_string(input_string):
    string_hash = []
    for character in input_string:
        if character in string_hash:
            return False
        else:
            string_hash.append(character)
    return True

# ... without using additional data structures
def unique_string_2(input_string):
    for i in range(len(input_string)):
        for c in input_string[i+1:]:
            if input_string[i] == c:
                return False
    return True

if __name__ == "__main__":
    unique = "abcde"
    not_unique ="abcda"
    
    assert unique_string(unique) == True
    assert unique_string(not_unique) == False
    assert unique_string_2(unique) == True
    assert unique_string_2(not_unique) == False
