"""
Exercise 4  
Modify reverse_lookup so that it builds and returns
a list of all keys that map to v, or an empty list if
there are none.
"""


def histogram(word):
    dictionary = dict()
    for c in word:
        if c not in dictionary:
            dictionary[c] = 1
        else:
            dictionary[c] = dictionary[c] + 1
    return dictionary


def reverse_lookup(histogram, value):
    lista = []
    for x in histogram:
        if histogram[x] == value:
            lista.append(x)
    return lista


print(reverse_lookup(histogram("pipi ponczoszanka"), 2))
