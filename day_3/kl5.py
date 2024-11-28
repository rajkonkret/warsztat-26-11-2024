# zrobić słownik z metodą która zwraca najdłuższy klucz w słowniku
class LongestKeyDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key

        return longest


# print(len(None)) # TypeError: object of type 'NoneType' has no len()
dictionary = LongestKeyDict()
print(dictionary.longest_key())  # None
dictionary['tomasz'] = 45
dictionary['abrahm'] = 7
dictionary['zen'] = 78
print(dictionary.longest_key())  # tomasz
