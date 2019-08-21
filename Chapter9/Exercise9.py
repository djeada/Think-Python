'''
Exercise 9
“Recently I had a visit with my mom and we realized that the
two digits that make up my age when reversed resulted in her
age. For example, if she’s 73, I’m 37. We wondered how often
this has happened over the years but we got sidetracked with
other topics and we never came up with an answer.
“When I got home I figured out that the digits of our ages have
been reversible six times so far. I also figured out that
if we’re lucky it would happen again in a few years, and if
we’re really lucky it would happen one more time after that.
In other words, it would have happened
8 times over all. So the question is, how old am I now?”
'''

def is_anagram(a,b):
    if str(a) == str(b)[::-1]:
        return True
    return False

def add_diff(dictionary, diff):
        if diff not in dictionary:
            dictionary[diff] = 1
        else:
            dictionary[diff] = dictionary[diff] + 1

def display_result(dictionary):
    for key in dictionary:
        print('For difference of ages', key, ' ages of daughter and mother would be anagrams', dictionary[key], ' times.')

def generate_ages():
    dictionary = dict()
    a = 10
    diff = 9
    while diff < 80:
        while a < 90: 
            if is_anagram(a,a+diff):
                add_diff(dictionary,diff)
            a += 1
        a = 10
        diff += 1

    display_result(dictionary)

generate_ages()

def how_old_is_she(diff):
    counter = 0
    for i in range(100):
        if is_anagram(i,i+diff):
            counter += 1
            if counter == 6:
                print('Daughter is now ', i, ' years old.')
                break

how_old_is_she(9)




