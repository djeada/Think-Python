'''
Exercise 7
This exercise is a cautionary tale about one of the most common, and difficult
to find, errors in Python. Write a definition for a class named Kangaroo with
the following methods:
An __init__ method that initializes an attribute named pouch_contents to an
empty list. A method named put_in_pouch that takes an object of any type and
adds it to pouch_contents. A __str__ method that returns a string
representation of the Kangaroo object and the contents of the pouch. Test your
code by creating two Kangaroo objects, assigning them to variables named kanga
and roo, and then adding roo to the contents of kanga’s pouch.
Download http://thinkpython.com/code/BadKangaroo.py. It contains a solution to
the previous problem with one big, nasty bug. Find and fix the bug.

If you get stuck, you can download http://thinkpython.com/code/GoodKangaroo.py, which explains the problem and demonstrates a solution.
'''

class Kangaroo(object):
    def __init__(self, pouch_contents=None):
        if pouch_contents == None:
            pouch_contents = []
        self.pouch_contents = pouch_contents


    def __str__(self):
        t = [ object.__str__(self) + ' with pouch contents:' ]

        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, obj):
        self.pouch_contents.append(obj)


kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch(24)
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
print("roo: ", roo)
