'''
Exercise 7
The datetime module provides date and time objects that are similar to the
Date and Time objects in this chapter, but they provide a rich set of methods
and operators. Read the documentation at
http://docs.python.org/2/library/datetime.html.

1. Use the datetime module to write a program that gets the current date and
prints the day of the week.
2. Write a program that takes a birthday as input and prints the user’s age and the number of days, hours, minutes and seconds until
their next birthday.
3. For two people born on different days, there is a day when one is twice as
old as the other. That’s their Double Day. Write a program that takes two
birthdays and computes their Double Day.
4. For a little more challenge, write the more general version that computes
the day when one person is n times older than the other.
'''

import datetime

def print_date_and_day_of_week():
    date = datetime.date.today()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(date, ' : ', days[date.weekday()])

print_date_and_day_of_week()

class Birthday():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

def time_to_next_birthday(b):
    birth = datetime.datetime(b.year, b.month, b.day)
    time = datetime.datetime.now()

    if (time.month, time.day) < (birth.month, birth.day):
        next_bday = (time.year, b.month, b.day)
    else:
        next_bday = (time.year + 1, b.month, b.day)

    print('your age: ', time.year - birth.year - ((time.month, time.day) < (birth.month, birth.day)))
    print('time to next birthday: ', (datetime.datetime(next_bday[0],next_bday[1],next_bday[2])-time).days, 'days ;)')

time_to_next_birthday(Birthday(1995,11,2))


def find_older(b1,b2):
    return (b1,b2) if (datetime.datetime(b1.year,b1.month,b1.day)-datetime.datetime(b2.year,b2.month,b2.day)).days < 0 else (b2,b1)

def return_date(date):
    return '%.2d-%.2d-%.2d' % (date.year, date.month, date.day)


def find_double_day(b1, b2):

    st = find_older(b1,b2)
    date = datetime.datetime(st[1].year,st[1].month,st[1].day)

    x = (datetime.datetime(st[1].year,st[1].month,st[1].day)-datetime.datetime(st[0].year,st[0].month,st[0].day)).days
    y = 0
    
    while x != 2*y:
        x+=1
        y+=1
        date += datetime.timedelta(days=1)

    print(return_date(date))
    print('Older guy was ', (date - datetime.datetime(st[0].year,st[0].month,st[0].day)).days, ' days old, and younger dude was ', (date - datetime.datetime(st[1].year,st[1].month,st[1].day)).days, ' days old')

find_double_day(Birthday(2012,7,18), Birthday(1997,6,12))

'''
def find_n_times_day(b.day1, b.day2, n):
    person1 = datetime.date(*b.day1)
    person2 = datetime.date(*b.day2)

    age_diff = -(person1 - person2)

    p1 = int(age_diff.days)
    p2 = 0

    while p2 * n != p1:
        if p2 * n > p1:
            print('This never precisely occurred')
            return None
        p1 += 1
        p2 += 1

    date_at_n_times_age = person2 + datetime.timedelta(days=p2)

    print(date_at_n_times_age, '\n', 'person 1 was %d days old, and person 2 was %d days old' % (p1, p2))
'''
