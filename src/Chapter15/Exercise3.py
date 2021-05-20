"""
Exercise 3 
Write a version of move_rectangle that creates and returns
a new Rectangle instead of modifying the old one.
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
    return Rectangle(
        rectangle.width,
        rectangle.height,
        Point(rectangle.corner.x + dx, rectangle.corner.y + dy),
    )


rectangle = Rectangle(100, 100, Point(5, 10))

print("Before moving: ")
print(rectangle.corner.x)
print(rectangle.corner.y)


rectangle2 = move_rectangle(rectangle, 20, 30)

print("After moving: ")
print(rectangle2.corner.x)
print(rectangle2.corner.y)
