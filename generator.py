def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)


# A Generator in Python is a function that returns an iterator using the Yield keyword. 
# A generator function in Python is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return.
