"""
Exercise 3  
Dictionaries have a method called keys that returns the
keys of the dictionary, in no particular order, as a list.

Modify print_hist toprint the keys and their values in
alphabetical order.
"""


def histogram(word):
    dictionary = dict()
    for c in word:
        if c not in dictionary:
            dictionary[c] = 1
        else:
            dictionary[c] = dictionary[c] + 1
    return dictionary


def print_hist(histogram):
    lista = []
    for x in histogram:
        lista.append((x, histogram[x]))

    lista.sort()
    for x in lista:
        print(x[0], x[1])


print_hist(histogram("pipi ponczoszanka"))
