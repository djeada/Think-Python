"""
Exercise 3  
Modify the program from the previous exercise to print the 20 most
frequently-used words in the book.
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


histo = {}
for word in word_list:
    histo[word] = histo.get(word, 0) + 1


def top_20(histo):
    lista = []
    for word in histo:
        lista.append((word, histo[word]))
    lista.sort(reverse=True)
    return [lista[i][0] for i in range(len(lista)) if i < 20]


print("Top 20 word :")
for x in top_20(histo):
    print(x)
