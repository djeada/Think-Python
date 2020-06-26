'''
Exercise 1  
Write a function called distance_between_points that takes two
Points as arguments and returns the distance between them.
'''

import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(3,8)
p2 = Point(5,9)

def distance_between_points(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

print(distance_between_points(p1,p2))
