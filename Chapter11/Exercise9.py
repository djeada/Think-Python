'''
Exercise 9
If you did Exercise 8,you already have a function named
has_duplicates that takes a list as a parameter and returns
True if there is any object that appears more than once in
the list.

Use a dictionary to write a faster, simpler version of
has_duplicates.
'''

def has_duplicates(word):
    dictionary = dict()
    for c in word:
        if c in dictionary:
            return True
        dictionary[c] = 1
    return False

print(has_duplicates('baba jaga'))
