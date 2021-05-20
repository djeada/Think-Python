"""
Exercise 3 
Write a function called snowflake that draws
three Koch curves to make the outline of 0a snowflake.
"""

import turtle


def koch(turtle, n):
    if n < 3:
        turtle.forward(n)
        return
    m = n / 3.0
    koch(turtle, m)
    turtle.left(60)
    koch(turtle, m)
    turtle.right(120)
    koch(turtle, m)
    turtle.left(60)
    koch(turtle, m)


def snowflake(turtle, n):
    for i in range(3):
        koch(turtle, n)
        turtle.right(120)


adam = turtle.Turtle()
adam.speed(100)

snowflake(adam, 300)

turtle.exitonclick()
