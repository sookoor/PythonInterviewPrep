# Sort an array of strings so that all the anagrams are next to each
# other.

def sort_by_anagram(string_array):
    return sorted(string_array, cmp = lambda x, y : cmp(sorted(str(x).replace(" ", "").lower()), sorted(str(y).replace(" ", "").lower())))

if __name__ == "__main__":
    assert sort_by_anagram(["Dormitory", "Dictionary", "Schoolmaster", "Elvis", "Listen", "Dirty Room", "Indicatory", "The classroom", "Lives", "Silent", "Clint Eastwood"]) == ['Clint Eastwood', 'Dictionary', 'Indicatory', 'Schoolmaster', 'The classroom', 'Dormitory', 'Dirty Room', 'Listen', 'Silent', 'Elvis', 'Lives']

    assert sort_by_anagram([3, 2, 1]) == [1, 2, 3]

    assert sort_by_anagram([]) == []
