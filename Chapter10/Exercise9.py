'''
Exercise 9
Write a function called remove_duplicates that takes a list and
returns a new list with only the unique elements from the original.
Hint: they don't have to be in the same order.
'''

def remove_duplicates(lista):
    return list(set(lista))

print(remove_duplicates([35,45,35,2,1,9,2,4]))
