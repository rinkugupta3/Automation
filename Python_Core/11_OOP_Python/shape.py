# interface - contract which has method signatures in python or an abract class
# Abract Base Class ABC

from abc import ABC, abstractmethod

# Define base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def closeconn(self):
        pass
'''
# Derived class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def closeconn(self):
        print("connection closed")

circle = Circle(5)

print(circle.area())
'''