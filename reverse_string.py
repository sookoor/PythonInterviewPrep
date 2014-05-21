# Code to reverse a C-Style String (e.g. "abcd" is represented as five characters, including the null character.)


def reverse_string_reversed(input_string):
    return "".join(reversed(input_string[:-1])) + input_string[-1]

def reverse_string_slice(input_string):
    return input_string[-2::-1] + input_string[-1]

input_string = "Madam I'm Adam\0"

assert reverse_string_slice(input_string) == reverse_string_reversed(input_string)
