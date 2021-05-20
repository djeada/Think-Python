"""
Exercise 7
This algorithm works, but it is not very efficient; each time you choose a
random word, it rebuilds the list, which is as big as the original book. An
obvious improvement is to build the list once and then make multiple selections,
but the list is still big.

An alternative is:

Use keys to get a list of the words in the book.
Build a list that contains the cumulative sum of the word frequencies
(see Exercise 3). The last item in this list is the total number of words
in the book, n.
Choose a random number from 1 to n. Use a bisection search (See Exercise 11) to
find the index where the random number would be inserted in the cumulative sum.
Use the index to find the corresponding word in the word list.
Write a program that uses this algorithm to choose a random word from the book.
"""
from string import punctuation, whitespace
from bisect import bisect
import random

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
        if not (c in punctuation or c in whitespace or c == ""):
            clean += c.lower()
    return clean


book = [clean_word(x) for x in book]

histo = {}
for word in book:
    histo[word] = histo.get(word, 0) + 1


def random_word(histo):
    words = []
    freqs = []
    total = 0

    for word in histo:
        total += histo[word]
        words.append(word)
        freqs.append(total)

    return words[bisect(freqs, random.randint(0, total - 1))]


print(random_word(histo))
