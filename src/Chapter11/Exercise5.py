"""
Exercise 5 
Read the documentation of the dictionary method setdefault and
use it to write a more concise version of invert_dict.
"""


def histogram(word):
    dictionary = dict()
    for c in word:
        if c not in dictionary:
            dictionary[c] = 1
        else:
            dictionary[c] = dictionary[c] + 1
    return dictionary


def invert_dict(histogram):
    inv = dict()
    for x in histogram:
        if histogram[x] not in inv:
            inv[histogram[x]] = list(x)
        else:
            inv[histogram[x]] = list(inv[histogram[x]]) + list(x)
    return inv


print(invert_dict(histogram("parrot")))
