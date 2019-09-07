'''
Exercise 4 
Write a “pure” version of increment that creates and returns a new Time object
rather than modifying the parameter.
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

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

time = Time(1,34,40)
print_time(time)
time2 = increment(time,21412414)
print_time(time2)
