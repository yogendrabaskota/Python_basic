# PARENT CLASS
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def eat(self):
        return f"{self.name} is eating"

# CHILD CLASS (Subclass) inheriting from Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def speak(self):                    # Same method as parent class
        return f"{self.name} says Woof!"

    def fetch(self):
        return f"{self.name} is fetching"

# Usage:
dog = Dog("Puppy", 4, "Bhusiya")
print(dog.speak())      
print(dog.eat())        
print(dog.fetch())      
print(f"{dog.name} is {dog.age} years old and is a {dog.breed}")  