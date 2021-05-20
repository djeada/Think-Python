"""
Exercise 1
Write a __cmp__ method for Time objects. Hint: you can use tuple comparison,
but you also might consider using integer subtraction.

"""


class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def __gt__(self, other):
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour and self.minute > other.minute:
            return True
        elif (
            self.hour == other.hour
            and self.minute == other.minute
            and self.second >= other.minute
        ):
            return True
        return False


time1 = Time(13, 53, 11)
time2 = Time(13, 55, 11)

print(time2 > time1)
