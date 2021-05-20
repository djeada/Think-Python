"""
Exercise 7
Two words are anagrams if you can rearrange the letters from one to
spell the other. Write a function called is_anagram that takes two
strings and returns True if they are anagrams.
"""


def count_freq(slowo):
    slownik = dict()
    for x in slowo:
        if x not in slownik:
            slownik[x] = 1
        else:
            slownik[x] = slownik[x] + 1
    return slownik


def is_anagram(a, b):
    if count_freq(a) == count_freq(b):
        return True
    return False


print(is_anagram("kajak", "ajkak"))
