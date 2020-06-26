'''
Exercise 2  
Write a boolean function called is_after that takes two Time objects, time1 and
time2, and returns True if time1 follows time2 chronologically
and False otherwise. Challenge: don’t use an if statement.
'''

class Time():
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

def is_after(time1, time2):
    return (time1.hour, time1.minute, time1.second) > (time2.hour, time2.minute, time2.second)

print(is_after(Time(1,34,40),Time(431,214142,40)))
