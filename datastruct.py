# LIST

week = ["sunday","monday","tuesday","wednesday","thursday","friday"]

print(week[0]) #sunday
print(week[4]) #thursday

week.append("saturday")
print(week)

week.remove("tuesday")
print(week)

# LIST COMPREHENSIONS
square = [x**2 for x in range(5)]
print(square)  #output: [0,1,4,9,16]


# TUPLES
point = (2, 3)
print(point[0])  # 2
person = ("ram", "shyam")
print(person[1])  # shyam
# Tuples are immutable; you cannot modify them directly

# Dictionaries
person = {"name": "bashyal", "age": 25}
print(person["name"])  # bashyal
person["age"] = 26
print(person)  # Output: {'name': 'bashyal', 'age': 26}
person["city"] = "New York"
print(person)  # Output: {'name': 'bashyal', 'age': 26, 'city': 'New York'}


#LIST TUPLES AND DICTIONARIES

print("\n\n")

a = 1
print("The type of a is ", type(a)) # Print type of a 
b = "1"
print("The type of b is ",type(b)) # Print type of b



c = "zuckerberg"
d = None
e = 1
f = True
print(c)
print(d)
print(e)
print(f)

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)


dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)

#List is written inside []
#Tuple is written inside ()
#Dictionary is written inside {}
 
# list: A list is an ordered collection of data with elements separated by a comma and
# enclosed within square brackets. Lists are mutable and can be modified after creation.

# Tuple: A tuple is an ordered collection of data with elements separated by a comma and
# enclosed within parentheses. Tuples are immutable and can not be modified after creation.

# dict: A dictionary is an unordered collection of data containing a key:value pair. 
# The key:value pairs are enclosed within curly brackets.

#SETS

color = {"red","green","blue","orange"}
print(color)
color.add("pink")
print(color)
print("green" in color)  #True
color.remove("red")
print(color)

