"""
Exercise 8
The (so-called) Birthday Paradox:

Write a function called has_duplicates that takes a list and returns
True if there is any element that appears more than once.
It should not modify the original list.

If there are 23 students in your class, what are the chances that
two of you have the same birthday? You can estimate this probability
by generating random samples of 23 birthdays and checking for matches.

Hint: you can generate random birthdays with the randint function
in the random module.
"""
import random


def count_freq(slowo):
    slownik = dict()
    for x in slowo:
        if x not in slownik:
            slownik[x] = 1
        else:
            slownik[x] = slownik[x] + 1
    return slownik


def has_duplicates(lista):
    slownik = count_freq(lista)
    for x in slownik:
        if slownik[x] > 1:
            return True
    return False


lista = []

for x in range(23):
    lista.append((random.randint(1, 31), random.randint(1, 12)))


slownik = count_freq(lista)
for x in slownik:
    print(x, " appeares ", slownik[x], " times.")

print(has_duplicates(lista))
