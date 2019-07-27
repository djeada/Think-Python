'''
Exercise 2
The Ackermann function, A(m, n), is defined:
See http://en.wikipedia.org/wiki/Ackermann_function.
Write a function named ack that evaluates Ackermann’s function.
Use your function to evaluate ack(3, 4), which should be 125.
What happens for larger values of m and n?
'''
def ackermann(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))

print(ackermann(3, 4))

