"""
Exercise 2  
Go to Project Gutenberg (http://gutenberg.org) and
download your favorite out-of-copyright book in plain
text format.

Modify your program from the previous exercise to read
the book you downloaded, skip over the header information
at the beginning of the file, and process the rest of the
words as before.

Then modify the program to count the total number of words
in the book, and the number of times each word is used.

Print the number of different words used in the book.
Compare different books by different authors, written in
different eras. Which author uses the most extensive vocabulary?
"""
from string import punctuation, whitespace

with open("pride_and_prejudice.txt", "r") as fd:
    for line in fd:
        if "Chapter " in line:
            word_list = [line.rstrip("\n")]
            for line in fd:
                line = line.rstrip("\n")
                word_list.append(line)


def clean_word(word):
    clean = ""
    for c in word:
        if not (c in punctuation or c in whitespace):
            clean += c.lower()
    return clean


word_list = [clean_word(x) for x in word_list]


hist = {}
for word in word_list:
    hist[word] = hist.get(word, 0) + 1

print("Total amount of words: %s" % len(word_list))
print("Unique words: %s" % len(hist))
