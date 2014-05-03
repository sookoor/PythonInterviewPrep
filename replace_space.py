import sys

def replace_space(string):
    return string.replace(" ", "%20")

def replace_space_manual(string):
    stringLength = len(string)
    num_spaces = string.count(" ")
    newLength = stringLength + 2 * num_spaces
    newStr = ['\n'] * newLength
    for i in range(len(string)-1,-1,-1):
        if string[i] == " ":
            newStr[newLength - 1] = '0'
            newStr[newLength - 2] = '2'
            newStr[newLength - 3] = '%'
            newLength -= 3
        else:
            newStr[newLength - 1] = string[i]
            newLength -= 1
    return ''.join(newStr)

def main():
    string = "Hello World"
    print replace_space_manual(string)

if __name__ == "__main__":
    status = main()
    sys.exit(status)
