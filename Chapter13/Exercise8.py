'''
Exercise 8
Markov analysis:

Write a program to read a text from a file and perform Markov analysis.
The result should be a dictionary that maps from prefixes to a collection of
possible suffixes. The collection might be a list, tuple, or dictionary; it
is up to you to make an appropriate choice. You can test your program with
prefix length two, but you should write the program in a way that makes it
easy to try other lengths.
Add a function to the previous program to generate random text based on the
Markov analysis. Here is an example from Emma with prefix length 2:
He was very clever, be it sweetness or be angry, ashamed or only amused, at
such a stroke. She had never thought of Hannah till you were never meant for
me?" "I cannot make speeches, Emma:" he soon cut it all himself.
For this example, I left the punctuation attached to the words. The result
is almost syntactically correct, but not quite. Semantically, it almost makes
sense, but not quite.

What happens if you increase the prefix length? Does the random text make more
sense?

Once your program is working, you might want to try a mash-up: if you analyze
text from two or more books, the random text you generate will blend the
vocabulary and phrases from the sources in interesting ways.
Credit: This case study is based on an example from Kernighan and Pike, The
Practice of Programming, Addison-Wesley, 1999.
'''
import sys
from string import punctuation, whitespace
import random

suffix_map = {}     
prefix = ()

with open('pride_and_prejudice.txt', 'r') as fd:
    for line in fd:
        if 'Chapter ' in line:
            word_list = [line.rstrip('\n')]
            for line in fd:
                line = line.rstrip('\n')
                word_list.append(line)

def clean_word(word):
    clean = ''
    for c in word:
        if not (c in punctuation or c in whitespace):
            clean += c.lower()
    return clean

def shift(t, word):
    return t[1:] + (word,)

def process_word(word, order=2):
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)
    except KeyError:
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)
    
word_list = [clean_word(x) for x in word_list]

for word in word_list:
    process_word(word)

def random_text(n=100):
    start = random.choice(list(suffix_map.keys()))
    
    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            random_text(n-i)
            return

        word = random.choice(suffixes)
        print(word)
        start = shift(start, word)

random_text()

