'''
Exercise 5 
Write an add method for Points that works with either a Point object or a tuple:
If the second operand is a Point, the method should return a new Point whose x
coordinate is the sum of the x coordinates of the operands, and likewise for
the y coordinates.
If the second operand is a tuple, the method should add the first element of
the tuple to the x coordinate and the second element to the y coordinate, and
return a new Point with the result.
'''

class Point():
    def __init__(self, x=5, y=5):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x coordinate: ' + str(self.x) + ' y coordinate: ' + str(self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other[0], self.y + other[1])


p1 = Point(3,8)
p2 = Point(3,8)
t = (3,9)
print(p1+p2)
print(p1+t)
