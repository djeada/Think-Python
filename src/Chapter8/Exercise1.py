'''
Exercise 1  
Write a function that takes a string as an argument and displays
the letters backward, one per line.
'''

def reverse1(s):
    if (len(s) <= 1):
        return s
    return reverse1(s[1:]) + s[0]

print(reverse1('Jamie'))

def reverse2(s):
    if (len(s) <= 1):
        return s
    return s[::-1]

print(reverse2('Jamie'))

def reverse3(s):
    if (len(s) <= 1):
        return s
    i = len(s)
    ret = ''
    while i > 0:
        ret = ret + s[i - 1]
        i -= 1
    return ret

print(reverse3('Jamie'))
