"""
Exercise5
This exercise can be done using only the statements and
other features we have learned so far.

Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

Hint: to print more than one value on a line, you can print
a comma-separated sequence:

print '+', '-'

If the sequence ends with a comma, Python leaves the line
unfinished, so the value printed next appears on the same line.

print '+', 
print '-'

The output of these statements is '+ -'.

A print statement all by itself ends the current line and
goes to the next line.

Write a function that draws a similar grid with four rows
and four columns.                                                              allen
"""


def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_plus():
    print("+", end="")


def print_line():
    print(" -", end="")


def print_column():
    print("|", end="")


def print_space():
    print(" ", end="")


def print_line_one():
    print_plus()
    do_four(print_line)
    print_space()


def print_line_two():
    do_twice(print_line_one)
    print_plus()
    print("")


def print_line_three():
    print_column()
    do_four(print_space)
    print_space()
    do_four(print_space)


def print_line_four():
    do_twice(print_line_three)
    print_column()
    print("")


def print_grid():
    print_line_two()
    do_four(print_line_four)
    print_line_two()
    do_four(print_line_four)
    print_line_two()


print_grid()
