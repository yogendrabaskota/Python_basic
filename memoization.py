from functools import lru_cache

@lru_cache(maxsize=None)

def fibon(n):
    if n < 2:
        return n 
    return fibon(n-1) + fibon(n-2)
print(fibon(5))
print(fibon(6))
print(fibon(8))
print(fibon(10))


# In the world of computer programming,Memoisation or Memoization in Python is a special kind of optimization technique that is primarily used to speed
#  up our computer program. It effectively reduces the runtime of the computer program by storing the results of the expensive
#  (in terms of runtime) function calls into the memory and using it whenever any stored or cached value is required.
