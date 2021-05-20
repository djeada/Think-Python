"""
Exercise 5
Write a function named uses_all that takes a word and a string of
required letters, and that returns True if the word uses all the
required letters at least once. How many words are there that use all
the vowels aeiou? How about aeiouy?
"""


def uses_all(word, string):
    count = 0
    for letter in string:
        if letter in word:
            count += 1
    if count == len(string):
        return True
    return False


with open("words.txt", "r") as fd:
    word_list = fd.read().splitlines()

words = [word for word in word_list if uses_all(word, "aeiou")]

print("There are {} words that use all {}".format(len(words), "aeiou"))

for word in words:
    print(word)
