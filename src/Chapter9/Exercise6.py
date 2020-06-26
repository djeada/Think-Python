'''
Exercise 6
Write a function called is_abecedarian that returns True if the
letters in a word appear in alphabetical order (double letters are ok).
How many abecedarian words are there?
'''

def is_abecedarian(word):
    return word == ''.join(sorted(word))

with open('words.txt', 'r') as fd:
    word_list = fd.read().splitlines()

words = [word for word in word_list if is_abecedarian(word)]

print('There are {} abecedarian words'.format(len(words)))

for word in words:
      print(word)






