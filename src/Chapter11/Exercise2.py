'''
Exercise 2  
Dictionaries have a method called get that takes a key and
a default value. If the key appears in the dictionary, get
returns the corresponding value; otherwise it returns the
default value. For example:

>>> h = histogram('a')
>>> print h
{'a': 1}
>>> h.get('a', 0)
1
>>> h.get('b', 0)
0
'''

def histogram(word):
    dictionary = dict()
    for c in word:
        if c not in dictionary:
            dictionary[c] = 1
        else:
            dictionary[c] = dictionary[c] + 1
    return dictionary

h = histogram('wifi')
print(h.get('i'))

