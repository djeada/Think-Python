'''
Exercise 2
Modify the program to fix this error.
'''

prefixes = 'JKLMNOPQ'
suffix = 'ack'

def ducks():
    for p in prefixes:
        if p in ['O', 'Q']:
            yield '{}uack'.format(p)
        else:
            yield '{}ack'.format(p)

for i in list(ducks()):
    print(i)


