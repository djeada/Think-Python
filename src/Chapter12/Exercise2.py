'''
Exercise 2 
In this example, ties are broken by comparing words, so words
with the same length appear in reverse alphabetical order.
For other applications you might want to break ties at random.
Modify this example so that words with the same length appear
in random order. Hint: see the random function in the random
module. 
'''

import random

def sort_by_length_random(words):
    t = []
    for word in words:
       t.append((len(word), random.random(), word))

    t.sort(reverse=True)

    res = []
    for length, _, word in t:
        res.append(word)
    return res

words = ['Tunczyk', 'Brokul', 'James', 'Pom','Tom', 'Banana']

for x in sort_by_length_random(words):
    print(x)
