'''
Exercise 1  
Write a function called print_time that takes a Time object and prints it in
the form hour:minute:second. Hint: the format sequence ‘%.2d’ prints an
integer using at least two digits, including a leading zero if necessary.
'''

import math

class Time():
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

print_time(Time(11,34,40))
