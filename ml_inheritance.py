# GRANDPARENT CLASS
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# PARENT CLASS INHERITED FROM ANIMAL GRANDPARENT CLASS)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# CHILD CLASS INHERITED FORM DOG (PARENT CLASS)
class Puppy(Dog):
    def fetch(self):
        return f"{self.name} is fetching"

# Usage:
puppy = Puppy("Max")
print(puppy.speak())    
print(puppy.fetch())    