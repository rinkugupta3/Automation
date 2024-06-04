# interface - contract which has method signatures in python or an abract class
# Abract Base Class ABC


from shape import Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

    def closeconn(self):
        print("connection closed")


circle = Circle(10)
print(circle.area())