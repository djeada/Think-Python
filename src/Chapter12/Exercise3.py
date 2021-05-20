"""
Exercise 3 
Write a function called most_frequent that takes a string and
prints the letters in decreasing order of frequency. Find text
samples from several different languagesand see how letter
frequency varies between languages. module. 
"""

with open("words.txt") as fd:
    word_list = fd.read().splitlines()


def add_to_dictionary(x, dictionary):
    if x not in dictionary:
        dictionary[x] = 1
    else:
        dictionary[x] = dictionary[x] + 1


def frequency(word_list):
    dictionary = dict()
    for word in word_list:
        for c in word:
            add_to_dictionary(c, dictionary)

    sorted_x = sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_x


for x in frequency(word_list)[:10]:
    print("Charachter ", x[0], " appeares ", x[1], " times.")
