"""
Exercise 2  
Write a function named move_rectangle that takes a Rectangle and two numbers
named dx and dy. It should change the location of the rectangle by adding dx
to the x coordinate of corner and adding dy to the y coordinate of corner.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner


def move_rectangle(rectangle, dx, dy):
    rectangle.corner.x += dx
    rectangle.corner.y += dy


rectangle = Rectangle(100, 100, Point(5, 10))

print("Before moving: ")
print(rectangle.corner.x)
print(rectangle.corner.y)


move_rectangle(rectangle, 20, 30)

print("After moving: ")
print(rectangle.corner.x)
print(rectangle.corner.y)
