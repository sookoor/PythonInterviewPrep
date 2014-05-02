def reverse_string_reversed(input_string):
    return "".join(reversed(input_string))

def reverse_string_slice(input_string):
    return input_string[::-1]

print reverse_string_slice("Madam I'm Adam")
