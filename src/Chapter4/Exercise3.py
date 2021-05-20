"""
Exercise 2
Write an appropriately general set of functions
that can draw shapes as in Figure 4.2.
"""
import math
import turtle
import time


def isosceles(turtle, radius, angle):
    y = radius * math.sin(angle * math.pi / 180)

    turtle.right(angle)
    turtle.forward(radius)
    turtle.left(90 + angle)
    turtle.forward(y * 2)
    turtle.left(90 + angle)
    turtle.forward(radius)
    turtle.right(180 + angle)


def draw_pie(turtle, radius, n):
    for i in range(n):
        isosceles(turtle, radius, int(180 / n))
        turtle.left(int(360 / n))


def move(turtle, length):
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()


adam = turtle.Turtle()
adam.speed(100)

move(adam, -300)

for i in range(1, 5):
    draw_pie(adam, i * 30, i * 5)
    move(adam, i * 90)

turtle.exitonclick()
