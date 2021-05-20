"""
Exercise 1  
Rewrite the function print_n from Section 5.8
using iteration instead of recursion.
"""

# recursive solution
def rec_print_n(s, n):
    if n <= 0:
        return
    print(s)
    rec_print_n(s, n - 1)


# itterative solution
def it_print_n(s, n):
    for i in range(n):
        print(s)


rec_print_n(10, 4)
it_print_n(10, 4)
