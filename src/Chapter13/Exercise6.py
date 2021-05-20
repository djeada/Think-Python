"""
Exercise 6
Python provides a data structure called set that provides many common set
operations. Read the documentation at
http://docs.python.org/2/library/stdtypes.html#types-set
and write a program that uses set subtraction to find words in the book that
are not in the word list.
"""
from string import punctuation, whitespace

with open("pride_and_prejudice.txt", "r") as fd:
    for line in fd:
        if "Chapter " in line:
            book = [line.rstrip("\n")]
            for line in fd:
                line = line.rstrip("\n")
                book.append(line)


def clean_word(word):
    clean = ""
    for c in word:
        if not (c in punctuation or c in whitespace):
            clean += c.lower()
    return clean


book = [clean_word(x) for x in book]

with open("words.txt") as fd:
    word_list = fd.read().splitlines()

book = set(book) - set(word_list)

for word in book:
    print(word)
