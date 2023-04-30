class Shape():
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return (self.radius**2) * 3.14

    def get_round(self):
        return self.radius * 2 * 3.14


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.width * self.length

    def get_round(self):
        return (self.width + self.length) * 2


cir = Circle(3)

print("넓이 :", cir.get_area())
print("둘레 :", cir.get_round())


rec = Rectangle(2, 73)

print("넓이 :", rec.get_area())
print("둘레 :", rec.get_round())
