'''
Exercise 1  
Write a function that reads the words in words.txt and
stores them as keys in a dictionary. It doesn’t matter what
the values are. Then you can use the in operator as a
fast way to check whether a string is in the dictionary.
'''

def function():
    with open('words.txt') as fd:
        words_list = fd.read().splitlines()

    dictionary = dict()
    
    for x in words_list:
        dictionary[x] = 1
    return dictionary

string = 'human'

if string in function():
    print('found')
else:
    print('not found')

