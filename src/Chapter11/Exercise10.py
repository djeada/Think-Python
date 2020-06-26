'''
Exercise 10
Two words are “rotate pairs” if you can rotate one of them
and get the other. Write a program that reads a wordlist and
finds all the rotate pairs. 
'''

with open('words.txt') as fd:
    word_list = fd.read().splitlines()

dictionary = {word: None for word in word_list}

def rotate_word(word, x):
    result = ''
    for c in word:
        c = ord(c) + x
        if c < ord('a'):
            c += 26
        elif c > ord('z'):
            c -= 26
        result = result + chr(c)
    return result

def rot_pairs(dictionary):
    lista = []
    for word in dictionary:
        for i in range(1, 14):
            rotated = rotate_word(word, i)
            if rotated in dictionary:
                lista.append((word, i, rotated))
    return lista

print(rot_pairs(dictionary))
