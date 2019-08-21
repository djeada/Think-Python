'''
Exercise 2  
Use capitalize_all to write a function named capitalize_nested that
takes a nested list of strings and returns a new nested list with
all strings capitalized.
'''

def capitalize_all(t):
    res = ''
    for s in t:
        res = res + s.capitalize()
    return res

def capitalize_nested(t):
    res = []
    for s in t:
        res.append(capitalize_all(s))
    return res

print(capitalize_nested(['fds','to prince all ad-din', 'and his Parrot']))
    
