"""
Exercise 5
The greatest common divisor (GCD) of a and b is the largest
number that divides both of them with no remainder.

One way to find the GCD of two numbers is based on
the observation that if r is the remainder when a is divided
by b,then gcd(a, b) = gcd(b, r). As a base case,
we can use gcd(a, 0) = a.

Write a function called gcd that takes parameters a and b
and returns their greatest common divisor.
"""


def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)


print(gcd(11, 24))
print(gcd(16, 160))
