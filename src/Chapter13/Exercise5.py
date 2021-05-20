"""
Exercise 5
Write a function named choose_from_hist that takes a histogram as defined in
Section 11.1 and returns a random value from the histogram, chosen with
probability in proportion to frequency. For example, for this histogram:

>>> t = ['a', 'a', 'b']
>>> hist = histogram(t)
>>> print hist
{'a': 2, 'b': 1}
your function should return ’a’ with probability 2/3 and ’b’ with probability
1/3.
"""

import random


def choose_from_hist(histo):
    list_ = []
    counter = 0
    for key in histo:
        counter += histo[key]
    for key in histo:
        histo[key] = histo[key] / counter

    return random.choices([key for key in histo], [histo[key] for key in histo], k=1)[0]


word_list = ["abaskva", "azkaban", "bodura", "lopunas"]

histo = {}
for word in word_list:
    for c in word:
        histo[c] = histo.get(c, 0) + 1

for key in histo:
    print(key, " appeares ", histo[key], " times.")


# Little check
new_hist = {}

for i in range(1000):
    x = choose_from_hist(histo)
    new_hist[x] = new_hist.get(x, 0) + 1

for key in new_hist:
    print(key, " appeares ", new_hist[key], " times.")
