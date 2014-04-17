def is_anagram(string1, string2):
    return sorted(string1.replace(" ", "").lower()) == sorted(string2.replace(" ", "").lower())


def main():
    string1 = "Nag a ram"
    string2 = "Anagram"
    string3 = "Foo"
    print is_anagram(string1, string2)
    print is_anagram(string1, string3)

if __name__ == "__main__":
    main()
