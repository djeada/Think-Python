"""
Exercise 4
More anagrams!

Write a program that reads a word list from a file
(see Section 9.1) and prints all the sets of words that
are anagrams.

Here is an example of what the output might look like:

['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']
Hint: you might want to build a dictionary that maps from a
set of letters to a list of words that can be spelled with
those letters. The question is, how can you represent the set
of letters in a way that can be used as a key?

Modify the previous program so that it prints the largest set of
anagrams first, followed by the second largest set, and so on.
In Scrabble a “bingo” is when you play all seven tiles in your
rack, along with a letter on the board, to form an eight-letter
word. What set of 8 letters forms the most possible bingos?
Hint: there are seven.
"""

with open("words.txt") as fd:
    word_list = fd.read().splitlines()


def add_to_dictionary(x, dictionary):
    if x not in dictionary:
        dictionary[x] = 1
    else:
        dictionary[x] = dictionary[x] + 1


def compare(dict1, dict2):
    if type(dict1) is str or type(dict2) is str:
        return False
    for x in dict1:
        for y in dict2:
            if x == y:
                if dict1[x] != dict2[y]:
                    return False
    return True


def anagrams(word_list):
    lista = []
    for word in word_list:
        dictionary = dict()
        for c in word:
            add_to_dictionary(c, dictionary)
        lista.append((word, dictionary))

    anagramy = [0 for i in range(max(len(x[0]) for x in lista) + 1)]
    for x in lista:
        if anagramy[len(x[0])] == 0:
            anagramy[len(x[0])] = x
        else:
            anagramy[len(x[0])] = anagramy[len(x[0])] + x

    for i in range(len(anagramy)):
        if 0 in anagramy:
            anagramy.remove(0)

    anagramy2 = []

    for x in anagramy:
        for i in range(len(x)):
            lista = []
            if type(x) is not str:
                for j in range(i, len(x)):
                    if compare(x[i], x[j]):
                        lista.append(x[j - 1])
                        if x[i - 1] not in lista:
                            lista.append(x[i - 1])
            if lista:
                anagramy2.append(lista)

    print(anagramy2[0])


anagrams(word_list)
