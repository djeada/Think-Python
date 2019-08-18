'''
Exercise 5
Encapsulate this code in a function named count,
and generalize it so that it accepts the string and
the letter as arguments.
'''

def count(word, target):
    i = 0
    for letter in word:
        if letter == target:
            i += 1
    return i

print(count('aleikum al ibdatu', 'i'))


