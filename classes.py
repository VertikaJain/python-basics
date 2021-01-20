# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Class creation
class User:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def myFunc(self):  # method
        return f"my name is {self.name} of age {self.age}"

    def birthday(self):
        self.age += 1


# Extend a class
class Customer(User):
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance
    
    def myFunc(self): # overwriting
        return f"my name is {self.name} of age {self.age} with balance = {self.balance}"


# Initialize object
obj = User("vertika jain", 24)
print(obj.name)
print(obj.age)
print(type(obj))
obj.birthday()
print(obj.myFunc())

obj2 = Customer("chandler", 30)
print(obj2.setBalance(500))
print(obj2.myFunc()) # can access method of upper class due to inheritance and overwrites in case same method name is defined.
