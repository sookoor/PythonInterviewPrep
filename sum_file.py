def sum_file(filename):
    file_sum = 0
    with open(filename, 'rb') as s_file:
        for num in s_file:
            file_sum += int(num)

    return file_sum

s = sum_file("ints.txt")
print "Sum: " + str(s)
