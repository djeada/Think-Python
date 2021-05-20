"""
Exercise 8
I was driving on the highway the other day and I happened to
notice my odometer. Like most odometers, it shows six digits,
in whole miles only. So, if my car had 300,000 miles,
for example, I’d see 3-0-0-0-0-0. Now, what I saw that day was
very interesting. I noticed that the last 4 digits were
palindromic; that is, they read the same forward as backward.
For example, 5-4-4-5 is a palindrome, so my odometer could have
read 3-1-5-4-4-5. One mile later, the last 5 numbers were
palindromic. For example, it could have read 3-6-5-4-5-6.
One mile after that, the middle 4 out of 6 numbers were
palindromic. And you ready for this? One mile later, all 6 were
palindromic! The question is, what was on the odometer when
I first looked?”
"""


def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    return False


def get_digits(num, start, finish):
    return int(str(num)[start : finish + 1])


def generate_Palindromes():
    lista = []
    number = 100000
    while number < 1000000:
        if is_palindrome(get_digits(number, 2, 5)):
            if is_palindrome(get_digits(number + 1, 1, 5)):
                if is_palindrome(get_digits(number + 2, 1, 4)):
                    if is_palindrome(number + 3):
                        lista.append(number)
        number += 1
    return lista


for x in generate_Palindromes():
    print(x)
