'''
Exercise 6
Write a function called is_sorted that takes a list as a parameter and
returns True if the list is sorted in ascending order and False
otherwise. You can assume (as a precondition) that the elements of the
list can be compared with the relational operators <, >, etc.
For example, is_sorted([1,2,2]) should return True
and is_sorted(['b','a']) should return False.
'''

def is_sorted(lista):
    for x in range(len(lista)-1):
        if not lista[x] <= lista[x+1]:
            return False
    return True

lista1 = [7, 2, 1, 0, 2, 32, 12, 1, 6, 21]
lista2 = [3, 6, 7, 7, 15, 18, 22, 111]


print(is_sorted(lista1))
print(is_sorted(lista2))

