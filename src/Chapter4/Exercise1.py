"""
Exercise 1  
Write appropriate docstrings for polygon, arc and circle.
Draw a stack diagram that shows the state of the program
while executing circle(bob, radius). You can do the arithmetic
by hand or add print statements to the code. The version of arc
in Section 4.7 is not very accurate because the linear
approximation of the circle is always outside the true circle.
As a result, the turtle ends up a few units away from the
correct destination. My solution shows a way to reduce the
effect of this error. Read the code and see if it makes sense
to you. If you draw a diagram, you might see how it works.
"""
import math
import turtle
import time


def polyline(turtle, length, n, angle):
    for i in range(n):
        turtle.forward(length)
        turtle.left(angle)
        # time.sleep(1)


def square(turtle, length):
    polyline(turtle, length, 4, 90)


def polygon(turtle, length, n):
    polyline(turtle, length, n, int(360 / n))


def arc(turtle, radius, angle):
    arc_length = 2 * math.pi * radius * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    turtle.left(step_angle / 2)
    polyline(turtle, step_length, n, step_angle)
    turtle.right(step_angle / 2)


def circle(turtle, radius):
    arc(turtle, radius, 360)


adam = turtle.Turtle()
adam.speed(1)
square(adam, 100)
polygon(adam, 50, 8)
circle(adam, 100)
turtle.exitonclick()
