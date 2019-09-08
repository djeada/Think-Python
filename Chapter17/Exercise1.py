'''
Exercise 1  
Rewrite time_to_int (from Section 16.4) as a method. It is probably not
appropriate to rewrite int_to_time as a method; what object you would
invoke it on?
'''

class Time():
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

print_time(Time(11,34,40).time_to_int())
