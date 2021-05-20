"""
Exercise 3
Modify your solution to Exercise 2 by adding an Entry widget and a second
button. When the user presses the second button, it should read a color name
from the Entry and use it to change the fill color of the circle. Use config
to modify the existing circle; don’t create a new one.

Your program should handle the case where the user tries to change the color
of a circle that hasn’t been created, and the case where the color name is
invalid.
"""

import tkinter

root = tkinter.Tk()
root.geometry("480x480")

c = tkinter.Canvas(root, height=300, width=350, bg="green")
c.pack()


def function(c):
    if not ("circle" in vars() or "circle" in globals()):
        global circle
        circle = c.create_oval(30, 30, 150, 150, fill="red")
    else:
        inputValue = textBox.get("1.0", "end-1c")
        try:
            c.itemconfig(circle, fill=inputValue)
        except:
            print("Uknown color")


textBox = tkinter.Text(root, height=2, width=10)
textBox.pack()
buttonCommit = tkinter.Button(
    root, height=1, width=10, text="Input Color", command=lambda: function(c)
)
buttonCommit.pack()

b = tkinter.Button(
    root,
    text="Draw a circle",
    width=10,
    bg="red",
    fg="white",
    command=lambda: function(c),
)
b.pack()

root.mainloop()
