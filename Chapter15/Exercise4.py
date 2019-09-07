'''
Exercise 4  
1. Write a function called draw_rectangle that takes a Canvas and a Rectangle
as arguments and draws a representation of the Rectangle on the Canvas.
2. Add an attribute named color to your Rectangle objects and modify
draw_rectangle so that it uses the color attribute as the fill color.
3. Write a function called draw_point that takes a Canvas and a Point as
arguments and draws a representation of the Point on the Canvas.
4. Define a new class called Circle with appropriate attributes and instantiate
a few Circle objects. Write a function called draw_circle that draws circles
on the canvas.
5. Write a program that draws the national flag of the Czech Republic. Hint:
you can draw a polygon like this:
points = [[-150,-100], [150, 100], [150, -100]]
canvas.polygon(points, fill=’blue’)
'''

import tkinter

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle():
    def __init__(self, canvas, width, height, corner, color):
        self = canvas.create_rectangle(corner.x,corner.y, corner.x+width, corner.y+height, fill=color)

class Triangle():
    def __init__(self, canvas, points):
        self = canvas.create_polygon(points, outline=None, fill='blue')

class Circle():
    def __init__(self, canvas, radius, center):
        self = canvas.create_oval(center.x,center.y, center.x+radius, center.y+radius, fill='red')

class Canvas():
    def __init__(self, width, height):
        self.width = width
        self.height = height

def draw_czech_republic_flag(canvas):
    Rectangle(canvas, 480, 240, Point(0,0), 'white')
    Rectangle(canvas, 480, 240, Point(0,240), 'red')
    Triangle(canvas,[[0,0], [200, 240], [0, 480]])

root = tkinter.Tk()
root.geometry('480x480')

canvas = Canvas(480,480)
canvas = tkinter.Canvas(root, width=canvas.width, height=canvas.height)
canvas.pack()
draw_czech_republic_flag(canvas)

root.mainloop()
