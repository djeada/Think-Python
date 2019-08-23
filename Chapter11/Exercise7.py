'''
Exercise 7
Memoize the Ackermann function from Exercise 5 and see
if memoization makes it possible to evaluate the function
with bigger arguments.
'''
def ack(M, N):
    if M == 0:
        return N + 1
    elif N == 0:
        return ack(M - 1, 1)
    else:
        return ack(M - 1, ack(M, N - 1))

    
print(ack(3,2))
