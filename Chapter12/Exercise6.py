'''
Exercise 6
Two words form a “metathesis pair” if you can transform one into the other
by swapping two letters; for example, “converse” and “conserve.” Write a
program that finds all of the metathesis pairs in the dictionary.
Hint: don’t test all pairs of words, and don’t test all possible swaps.
'''

with open('words.txt') as fd:
    word_list = fd.read().splitlines()

def all_metathesis(word_list):
    lista = []
    for i in range(len(word_list)):
        for j in range(i+1,len(word_list)-1):
            if metathesis_pair(word_list[i], word_list[j]):
                   lista.append((word_list[i], word_list[j]))
    return lista

def metathesis_pair(word1, word2):
    if len(word1) == len(word2):
        if word_distance(word1, word2) == 2:
            if anagrams(list(word1), list(word2)):
                return True
    return False

def anagrams(word1,word2):
    word1.sort()
    word2.sort()

    i = 0
                   
    while i < len(word1):
        if word1[i]==word2[i]:
            i += 1
        else:
            return False

    return True

def word_distance(word1, word2):
    assert len(word1) == len(word2)

    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1

    return count


print(metathesis_pair('converse', 'conserve'))
print(all_metathesis(word_list))

