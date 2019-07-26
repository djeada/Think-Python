'''
Exercise 2
Write an appropriately general set of functions that can draw flowers as in Figure 4.1.
'''
import math
import turtle
import time
        
def polyline(turtle, length, n, angle):
    for i in range(n):
        turtle.forward(length)
        turtle.left(angle)

def arc(turtle, radius, angle):
    arc_length = 2 * math.pi * radius * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    turtle.left(step_angle/2)
    polyline(turtle, step_length, n, step_angle)
    turtle.right(step_angle/2)

def petal(turtle, radius, angle):
    for i in range(2):
        arc(turtle, radius, angle)
        turtle.left(180-angle)

def flower(turtle, radius, n, angle):
    for i in range(n):
        petal(turtle, radius, angle)
        turtle.left(int(360/n))

def move(turtle, length):
    #Pull the pen up – no drawing when moving.
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()

adam = turtle.Turtle()
adam.speed(100)

move(adam, -200)
flower(adam, 60.0, 7, 60.0)

move(adam, 200)
flower(adam, 30.0, 10, 100.0)

move(adam, 200)
flower(adam, 200.0, 40, 20.0)

turtle.exitonclick()


