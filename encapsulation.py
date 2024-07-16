class employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        self.__id = 6

    def get_details(self):
        return f"Name: {self.name} and salary {self._salary}"
    
    def _protected_method(self):
        print("This is protected method")

    def __private_method(self):
        print("This is private method")

    def access_private_method(self):
        self.__private_method()
    


emp = employee("ram", 500)

print(emp.name)

print(emp._salary)

try:
    print(emp.__id)
except AttributeError as e:
    print(f'{e} and error code is {id(e)}')

print(emp._employee__id)  

emp._protected_method()

try:
    emp._private_method()
except AttributeError as e :
    print(f'{e} and error code is {id(e)}')


emp._employee__private_method()

emp.access_private_method()


    