'''
Exercise 4 
Write an add method for the Point class.
'''

class Point():
    def __init__(self, x=5, y=5):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x coordinate: ' + str(self.x) + ' y coordinate: ' + str(self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(3,8)
p2 = Point(3,8)
print(p1+p2)

