# FIRST PARENT CLASS
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} is speaking"

# SECOND PARENT CLASS
class Mammal:
    def __init__(self, age):
        self.age = age
    
    def eat(self):
        return f"Mammal is eating"


# Child class inheriting from Animal class and Mammal class

class Dog(Animal, Mammal):
    def __init__(self, name, age, breed):
        Animal.__init__(self, name)  
        Mammal.__init__(self, age)   
        self.breed = breed           
    
    def bark(self):
        return f"{self.name} says Woof!"

# Usage:
dog = Dog("Puppy", 4, "Bhusiya")
print(dog.speak())    
print(dog.eat())      
print(dog.bark())     
print(f"{dog.name} is {dog.age} years old and is a {dog.breed}")  