import sys
import random

def largest_manual(integer_array):
    max_int = -sys.maxint - 1
    for i in integer_array:
        if i > max_int:
            max_int = i

    return max_int

random_array = [random.randint(0, 10) for i in range(0, 10)]
print random_array
print largest_manual(random_array)
print max(random_array)
