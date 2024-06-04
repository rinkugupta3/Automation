# Polymorphism - ability of object to take an multiple forms.

# Base class or supper class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass # Placeholder method, to be overriden by derived class or sub class


# Derived class - Interitance features of Animal class
class Pig(Animal):
    def make_sound(self): # polymorphism
        return "Baaa Baaa!"


class Cat(Animal):
    def make_sound(self): # polymorphism
        return "Meow Meow!"

# drived class
class Dog(Animal):
    def __init__(self, breed, age):
        super().__init__("Leo") # calling superclass
        self.bread = breed
        self.age = age
    def make_sound(self):
        return "Bhow! Bhow!"


pig = Pig("Buddy")
cat = Cat("Alexis")
dog = Dog("Corgi",3)

print(dog.name)
print(dog.bread)
print(dog.age)

# make a list
animals = [dog, cat]

for animal in animals:
    print(f"{animal.name} says {animal.make_sound()}")