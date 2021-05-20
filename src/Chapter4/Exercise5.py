"""
Exercise 2
Read about spirals at http://en.wikipedia.org/wiki/Spiral;
then write a program that draws an Archimedian spiral
(or one of the other kinds).
"""
import math
import turtle


def draw_spiral(turtle, n):
    for i in range(n):
        t = i / 20 * 3.14
        x = (1 + 5 * t) * math.cos(t)
        y = (1 + 5 * t) * math.sin(t)
        turtle.goto(x, y)


adam = turtle.Turtle()
# adam.speed(100)

draw_spiral(adam, 300)

turtle.exitonclick()
