"""
Exercise 5
Write a function called chop that takes a list, modifies it by
removing the first and last elements, and returns None.
"""


def chop(lista):
    del lista[0]
    del lista[-1]


lista = [1, 2, 3, 4]
chop(lista)
print(lista)
