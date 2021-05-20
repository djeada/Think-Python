"""
Exercise 1  
Write a function that takes a list of numbers and returns the
cumulative sum; that is, a new list where the ith element is the
sum of the first i + 1 elements from the original list. For example,
the cumulative sum of [1, 2, 3] is [1, 3, 6].
"""


def cumulative_sum(lista):
    cumulative = []
    total = 0
    for i in lista:
        total += i
        cumulative.append(total)
    return cumulative


print(
    "For list ",
    [12, 5, 9, 11],
    "the cumulative sum is ",
    cumulative_sum([12, 5, 9, 11]),
)
