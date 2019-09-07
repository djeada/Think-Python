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

def time_to_next_birthday(byear, bmonth, bday):
    birth = datetime.datetime(byear, bmonth, bday)
    time = datetime.datetime.now()

    if (time.month, time.day) < (birth.month, birth.day):
        next_bday = (time.year, bmonth, bday)
    else:
        next_bday = (time.year + 1, bmonth, bday)

    print('current age: ', time.year - birth.year - ((time.month, time.day) < (birth.month, birth.day)))
    print('time to next birthday: ', datetime.datetime(*next_bday) - time)

def find_double_day(bday1, bday2):

    person1 = datetime.date(*bday1)
    person2 = datetime.date(*bday2)

    age_diff = -(person1 - person2)

    p1 = int(age_diff.days)
    p2 = 0

    while p2 * 2 != p1:
        p1 += 1
        p2 += 1

    date_at_twice_age = person2 + datetime.timedelta(days=p2)
    print(date_at_twice_age, '\n', 'person 1 was %d days old, and person 2 was %d days old' % (p1, p2))

def find_n_times_day(bday1, bday2, n):
    person1 = datetime.date(*bday1)
    person2 = datetime.date(*bday2)

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
