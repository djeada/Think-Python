'''
Exercise 6
Write a function called mul_time that takes a Time object and a multber and
returns a new Time object that contains the product of the original Time and
the multber. Then use mul_time to write a function that takes a Time object
that represents the finishing time in a race, and a multber that represents
the distance, and returns a Time object that represents the average pace
(time per mile).
'''

class Time():
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

def increment(time, seconds):
    time2 = Time(time.hour,time.minute,time.second)
    time2.second += seconds

    add_mins, remain_seconds = divmod(time2.second, 60)
    time2.minute += add_mins
    time2.second = remain_seconds

    add_hours, remain_minute = divmod(time2.minute, 60)
    time2.hour += add_hours
    if time2.hour > 23:
        time2.hour = time2.hour%24
    time2.minute = remain_minute

    return time2

def to_sec(time):
    return time.hour*3600 + time.minute*60 + time.second

def find_average_pace(time, distance):
    return increment(Time(0,0,0), distance/to_sec(time))

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

time = Time(1,34,40)
print_time(find_average_pace(time,31012311))
