"""
Exercise 3 
Write a str method for the Point class. Create a Point object and print it.
"""


class Point:
    def __init__(self, x=5, y=5):
        self.x = x
        self.y = y

    def __str__(self):
        return "x coordinate: " + str(self.x) + " y coordinate: " + str(self.y)


p1 = Point(3, 8)
print(p1)
