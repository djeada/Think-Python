"""
Exercise 3  
To test the square root algorithm in this chapter,
you could compare it with math.sqrt.
Write a function named test_square_root that prints a table like this:
The first column is a number, a; the second column is the square root
of a computed with the function from Section 7.5; the third column is
the square root computed by math.sqrt; the fourth column is the
absolute value of the difference between the two estimates.
"""
import math

# implementation of newtons algorithm
def test_square_root(n):
    n = float(n)
    x = n / 2
    i = 0
    while i < 10:
        y = (x + n / x) / 2
        x = y
        i += 1
    return y


for i in range(1, 10):
    a = test_square_root(i)
    b = float(math.sqrt(i))
    c = abs(a - b)
    print("{0:.5f}\t".format(a), "{0:.5f} ".format(b), "{0:.5f}".format(c))
