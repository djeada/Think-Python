'''
Exercise 4  
Modify the previous program to read a word list (see Section 9.1) and then
print all the words in the book that are not in the word list. How many of
them are typos? How many of them are common words that should be in the word
list, and how many of them are really obscure?
'''
from string import punctuation, whitespace

with open('pride_and_prejudice.txt', 'r') as fd:
    for line in fd:
        if 'Chapter ' in line:
            book = [line.rstrip('\n')]
            for line in fd:
                line = line.rstrip('\n')
                book.append(line)

def clean_word(word):
    clean = ''
    for c in word:
        if not (c in punctuation or c in whitespace):
            clean += c.lower()
    return clean
        
book = [clean_word(x) for x in book]

with open('words.txt') as fd:
    word_list = fd.read().splitlines()

book = [word for word in book if word not in word_list]

for word in book:
    print(word)
