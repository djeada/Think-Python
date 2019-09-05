'''
Exercise 9
The “rank” of a word is its position in a list of words sorted by frequency: the most common word has rank 1, the second most common
has rank 2, etc.

Zipf’s law describes a relationship between the ranks and frequencies of words in natural languages
(http://en.wikipedia.org/wiki/Zipf's_law). Specifically, it predicts
that the frequency, f, of the word with rank r is:

f = c r^−s 
where s and c are parameters that depend on the language and the text. If you take the logarithm of both sides of this equation,
you get:

logf = logc − s logr 
So if you plot log f versus log r, you should get a straight line with slope −s and intercept log c.

Write a program that reads a text from a file, counts word frequencies, and prints one line for each word, in descending order of
frequency, with log f and log r. Use the graphing program of your choice to plot the results and check whether they form a straight
line. Can you estimate the value of s?
'''
from string import punctuation, whitespace
import random
import matplotlib.pyplot as plt
import math

suffix_map = {}     
prefix = ()

with open('words.txt') as fd:
    dictionary = fd.read().splitlines()

with open('pride_and_prejudice.txt', 'r') as fd:
    for line in fd:
        if 'Chapter ' in line:
            word_list = [line.rstrip('\n')]
            for line in fd:
                line = line.rstrip('\n')
                word_list.append(line.split())


def clean_word(word):
    clean = ''
    for c in word:
        if c in punctuation or c in whitespace:
            return
        else:
            clean += c.lower()
    return clean
    
word_list = [clean_word(y) for x in word_list for y in x]
word_list = list(filter(None, word_list))

histo = {}
for word in word_list:
    histo[word] = histo.get(word, 0) + 1

lista = []
for x in histo:
    lista.append((histo[x],x))

lista.sort(reverse=True)
print(lista[:10])

x = [math.log(x[0]) for x in lista]
y = [math.log(i) for i in range(1,len(lista)+1)]

plt.plot(x,y)
plt.show()

