'''
Exercise 10
Write a function that reads the file words.txt and builds a list
with one element per word. Write two versions of this function,
one using the append method and the other using the idiom t = t + [x].
Which one takes longer to run? Why?
'''
import time

with open('words.txt', 'r') as fd:
    word_list = fd.read().splitlines()

def appending(word_list):
    lista = []
    for word in word_list:
        lista.append(word.strip())

def concatenating(word_list):
    lista = []
    for word in word_list:
        lista = lista + [word]

start = time.time()
appending(word_list)
end = time.time()
a = end - start

start = time.time()
concatenating(word_list)
end = time.time()
b = end - start

print('Time for exectuion first function: ', a)
print('Time for exectuion second function: ', b)



