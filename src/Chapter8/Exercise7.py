"""
Exercise 7
There is a string method called count that is similar to the
function in the previous exercise. Read the documentation
of this method and write an invocation that counts the
number of as in 'banana'.
"""


def count(word, letter):
    return word.count(letter)


print(count("banana", "a"))
