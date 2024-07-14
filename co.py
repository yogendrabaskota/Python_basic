class my:
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll  


    
profile1 = my("Sujan baskota", 22, "45")
p2 = my("ram", 44, "23")

print(f'name: {profile1.name} \n age is : {profile1.age} \n and roll no is {profile1.roll}')
print(f'name: {p2.name} \n age is : {p2.age} \n and roll no is {p2.roll}')

