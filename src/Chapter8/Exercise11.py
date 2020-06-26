'''
Exercise 11
The following functions are all intended to check whether
a string contains any lowercase letters, but at least some
of them are wrong. For each function, describe what the
function actually does(assuming that the parameter is a string).
'''

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

#this function will terminte too soon becouse if the first
#letter is upper then it will already return False 

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

#this function doesnt return booleans but strings
#it will always return 'True'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

#this function will only tell us if the last letter is lowercase

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
    
#after finding one uppercase letter it will always return True

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
        
#this function check if every letter is lowercase 

print(any_lowercase1('taBaluga'))
print(any_lowercase2('taBaluga'))
print(any_lowercase3('taBaluga'))
print(any_lowercase4('taBaluga'))
print(any_lowercase5('taBaluga'))
