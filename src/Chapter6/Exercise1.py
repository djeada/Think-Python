'''
Exercise 1  
Draw a stack diagram for the following program.
What does the program print?
'''

from swampy.Lumpy import Lumpy

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    lumpy.object_diagram()
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

lumpy = Lumpy()
lumpy.make_reference()

x = 1
y = x + 1
print(c(x, y+3, x+y))
