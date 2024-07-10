#DEFINING FUNCTION IN PYTHON:

def person(name):
    return f"Hello {name}"

def add(a,b=5):  #function with argument
    return f"sum is {a+b}"

print(person("Yogendra"))
print(add(2))  # add 2 with default value 5
print(add(6,8)) # add 6 with 8 , ignore default valur


# LAMBDA FUNCTION
print("\nLambda function")
mul = lambda x,y : x * y
print(mul(5,6))
print(f"The multiplicatioin is {mul(5,6)}")


