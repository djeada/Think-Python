'''
Exercise 1  
The os module provides a function called walk that is similar to this one
but more versatile. Read the documentation and use it to print the names
of the files in a given directory and its subdirectories.
'''

import os

def walk(directory):
    names = []
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isfile(path):
            names.append(path)
        else:
            walk(path)
    for name in names:
        print(name)

walk(os.getcwd())
