"""
Exercise 1  
Many of the built-in functions use variable-length argument
tuples. For example, max and min can take any number of
arguments:

>>> max(1,2,3)
3
But sum does not.

>>> sum(1,2,3)
TypeError: sum expected at most 2 arguments, got 3
Write a function called sumall that takes any number
of arguments and returns their sum.
"""


def sumall(*args):
    return sum(args)


print(sumall(5, 9, 2))
print(sumall(15, 23, 343, 43))
print(sumall(234, 5, 9, 8, 4, 3, 0, 23))
