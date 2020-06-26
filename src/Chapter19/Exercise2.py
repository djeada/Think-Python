'''
Exercise 2
Write a program that creates a Canvas and a Button.
When the user presses the Button, it should draw a circle on the canvas.
'''

import tkinter

root = tkinter.Tk()
root.geometry('480x480')

c = tkinter.Canvas(root, height=300, width=350, bg='green')
c.pack()

def function(c):
    c.create_oval(30,30, 150, 150, fill='red')

b = tkinter.Button(root, text='Button', width=10, bg='red', fg='white', command=lambda: function(c))
b.pack()

root.mainloop()
