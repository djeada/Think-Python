"""
Exercise 5 
Rewrite increment using time_to_int and int_to_time.
"""


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time(0, 0, 0)
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    if time.hour > 23:
        time.hour = time.hour % 24
    return time


def increment(time, seconds):
    time = time_to_int(time) + seconds
    return int_to_time(time)


def print_time(time):
    print("%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))


time = Time(1, 34, 40)
print_time(time)
time2 = increment(time, 21412414)
print_time(time2)
