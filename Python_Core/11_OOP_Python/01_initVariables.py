class Person:
    def __init__(self,name ="Dhiraj",age=44):
        # attributes - characteristics of the object
        self.name = name
        self.age = age

# self parameters refers to the current instance of the class.

# Object is an instance of class person

person1 = Person("Alice",30)
person2 = Person()
print(person2.name)
print(person2.age)
