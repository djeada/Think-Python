"""
Exercise 6
Download the code from this chapter (http://thinkpython.com/code/Time2.py).
Change the attributes of Time to be a single integer representing seconds
since midnight. Then modify the methods (and the function int_to_time) to
work with the new implementation. You should not have to modify the test
code in main. When you are done, the output should be the same as before.
"""


class Time(object):
    """Represents the time of day.

    attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.second = (((hour * 60) + minute) * 60) + second

    def __str__(self):
        minutes, seconds = divmod(self.second, 60)
        hours, minutes = divmod(minutes, 60)
        return "%.2d:%.2d:%.2d" % (hours, minutes, seconds)

    def print_time(self):
        print(self)

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        return self.second

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.time_to_int() > other.time_to_int()

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.second + other.second
        return int_to_time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.second
        return int_to_time(seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        if self.second >= 86400 or self.second < 0:
            return False
        return True


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    return Time(0, 0, seconds)


def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print("Is end after start?")
    print(end.is_after(start))

    print("Using __str__")
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print("Example of polymorphism")
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


main()
