'''
Exercise 3 
Write a correct version of increment that doesn’t contain any loops.
'''

class Time():
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

def increment(time, seconds):
    time.second += seconds

    add_mins, remain_seconds = divmod(time.second, 60)
    time.minute += add_mins
    time.second = remain_seconds

    add_hours, remain_minute = divmod(time.minute, 60)
    time.hour += add_hours
    if time.hour > 23:
        time.hour = time.hour%24
    time.minute = remain_minute

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

time = Time(1,34,40)
print_time(time)
increment(time,21412414)
print_time(time)
