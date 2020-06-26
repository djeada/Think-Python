'''
Exercise 1
Write a program that creates a GUI with a single button. When the button is
pressed it should create a second button. When that button is pressed, it
should create a label that says, “Nice job!”.
'''

import tkinter

root = tkinter.Tk()
root.geometry('480x480')

def function(root):
    l = tkinter.Label(root, text='Nice job')
    l.pack()

b = tkinter.Button(root, text='Button', width=10, bg='red', fg='white', command=lambda: function(root))
b.pack()


root.mainloop()
