class animal :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def eat(self):
        return f'{self.name} eat this'
    

class dog(animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def bark(self):
        return f'{self.name} is barking'
    
    def fetch(self):
        return f'{self.name} is fetching'
    
d = dog("puppy", 4, "bhouu")

print(d.description())
print(d.eat())
print(d.bark())
print(d.fetch())

e = animal("ssecondDog", 5)

print(e.eat())
print(e.description())
try:
    print(e.bark())
except AttributeError as e:
    print(e)

