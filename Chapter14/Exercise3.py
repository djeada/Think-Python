'''
Exercise 3
Write a module that imports anagram_sets and provides two new functions:
store_anagrams should store the anagram dictionary in a “shelf;”
read_anagrams should look up a word and return a list of its anagrams. 
'''

with open('words.txt') as fd:
    word_list = fd.read().splitlines()

def add_to_dictionary(x, dictionary):
    if x not in dictionary:
        dictionary[x] = 1
    else:
        dictionary[x] = dictionary[x] + 1

def compare(dict1,dict2):
    if type(dict1) is str or type(dict2) is str:
        return False
    for x in dict1:
        for y in dict2:
            if x == y:
                if dict1[x] != dict2[y]:
                    return False
    return True

def anagrams(word_list):
    lista = []
    for word in word_list:
        dictionary = dict()
        for c in word:
            add_to_dictionary(c,dictionary)
        lista.append((word,dictionary))

    anagramy = [0 for i in range(max(len(x[0]) for x in lista)+1)]
    for x in lista:
        if anagramy[len(x[0])] == 0:
            anagramy[len(x[0])] = x
        else:
            anagramy[len(x[0])] = anagramy[len(x[0])] + x

    for i in range(len(anagramy)):
        if 0 in anagramy:
            anagramy.remove(0)
            
    anagramy2 = []
    
    for x in anagramy:
        for i in range(len(x)):
            lista = []
            if type(x) is not str:
                for j in range(i,len(x)):
                    if compare(x[i],x[j]):
                        lista.append(x[j-1])
                        if x[i-1] not in lista:
                            lista.append(x[i-1])
            if lista:
                anagramy2.append(lista)
    
    return anagramy2
    
def store_anagrams(filename, ad):

    shelf = shelve.open(filename, 'c')

    for word, word_list in ad.iteritems():
        shelf[word] =  word_list

    shelf.close()

def read_anagrams(filename, word):
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []


store_anagrams('anagrams.db', anagrams(word_list))
print(read_anagrams('anagrams.db', 'kayak'))
