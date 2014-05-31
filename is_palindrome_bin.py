import math

def is_palindrome_bin(n):
    if type(n) is not int:
        raise RuntimeError("n is not an int")

    try:
        num_bits = math.floor(math.log(n, 2)) + 1
    except ValueError:
        raise

    for i in range(num_bits):
        mask1 = 1
        mask1 = mask1 << i

        mask2 = 1
        left_offset = num_bits - i - 1
        mask2 = mask2 << left_offset

        if (n & mask1) >> i != (n & mask2) >> left_offset:
            return False
    return True

if __name__ == "__main__":
    assert is_palindrome_bin(1) == True
    assert is_palindrome_bin(2) == False
    assert is_palindrome_bin(3) == True
    assert is_palindrome_bin(4) == False
    assert is_palindrome_bin(5) == True

    try:
        is_palindrome_bin(0)
    except ValueError:
        print("Does not work for zero")
