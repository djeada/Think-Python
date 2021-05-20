"""
Exercise 4
Write a function named uses_only that takes a word and a string of
letters, and that returns True if the word contains only letters in
the list. Can you make a sentence using only the letters acefhlo?
Other than “Hoe alfalfa?”
"""


def uses_only(word, string):
    for letter in word:
        if letter not in string:
            return False
    return True


with open("words.txt", "r") as fd:
    word_list = fd.read().splitlines()

words = [word for word in word_list if uses_only(word, "acefhlo")]

print("There are {} words that use only {}".format(len(words), "acefhlo"))

for word in words:
    print(word)
