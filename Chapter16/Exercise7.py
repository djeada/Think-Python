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
    return (b1.year,b1.month,b1.day) > (b2.year,b2.month,b2.day) ? (b1,b2) : (b2,b1)

def find_double_day(b1, b2):

    st = find_older(b1,b2)

    if st[0].year < st[1].year:
        x = st[0].day + 365*(st[0].day-st[1].day)
        y = st[1].day
        while x != 2*y
            x+=1
            y+=1
        x = 

    elif st[0].month < st[2].year:
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)
    else:
    

    date_at_twice_age = person2 + datetime.timedelta(days=p2)
    print(date_at_twice_age, '\n', 'person 1 was %d days old, and person 2 was %d days old' % (p1, p2))

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
