'''
Exercise 12
Two words are a “reverse pair” if each is the reverse of the other.
Write a program that finds all the reverse pairs in the word list.
'''
with open('words.txt', 'r') as fd:
    word_list = fd.read().splitlines()


def reverse_pairs(lista):
    reverse_list = []
    maksimum = len(lista)
    i = 1
    for x in range(maksimum):
        while i < maksimum:
            if str(lista[x]) == str(lista[i])[::-1]:
                reverse_list.append((lista[x],lista[i]))
                del lista[i]
                maksimum -=1
            i += 1
        i=x+1
    return reverse_list
                
print(reverse_pairs(word_list))



