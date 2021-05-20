"""
Exercise 1  
Write a program that reads a file, breaks each line into words, strips
whitespace and punctuation from the words, and converts them to lowercase.

Hint: The string module provides strings named whitespace, which contains
space, tab, newline, etc., and punctuation which contains the punctuation
characters. Let’s see if we can make Python swear:

>>> import string
>>> print string.punctuation
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
Also, you might consider using the string methods strip, replace and translate.
"""
from string import punctuation, whitespace

with open("pride_and_prejudice.txt", "r") as fd:
    word_list = fd.read().split()


def clean_word(word):
    clean = ""
    for c in word:
        if not (c in punctuation or c in whitespace):
            clean += c.lower()
    return clean


word_list = [clean_word(x) for x in word_list]


print(word_list[-10:])
