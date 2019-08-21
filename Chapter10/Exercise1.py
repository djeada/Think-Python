'''
Exercise 1  
Write a function called nested_sum that takes a nested list of
integers and add up the elements from all of the nested lists.
'''

def add_all(t):
    total = 0
    for x in t:
        total += x
    return total

def nested_sum(lista):
    total = 0
    for x in lista:
        total += add_all(x)
    return total

lista = [[12, 5, 9, 11], [32, 11, 32], [99,12, 435]]
print('For list ', lista, 'the nested sum is ', nested_sum(lista))
