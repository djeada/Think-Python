"""
Exercise 2  
Write an init method for the Point class that takes x and y as
optional parameters and assigns them to the corresponding attributes.
"""


class Point:
    def __init__(self, x=5, y=5):
        self.x = x
        self.y = y


p1 = Point(3, 8)
p2 = Point(5, 9)
