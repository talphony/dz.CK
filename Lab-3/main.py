class GeometricShape:
    def __init__(self, name):
        self.name = name
    def area(self):
        return 0

class Rectangle(GeometricShape):
    def __init__(self, name, width, height ):
        super().__init__(name)
        self.width = width
        self.height = height
    def area(self):
        rectangle = self.width * self.height
        return rectangle

class Circle(GeometricShape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    def area(self):
        circle = (self.radius * self.radius) * 3.14
        return circle

class Rhombus(GeometricShape):
    def __init__(self, name, diagonal1, diagonal2):
        super().__init__(name)
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
    def area(self):
        rhombus = self.diagonal1 * self.diagonal2 * 0.5
        return rhombus

rec = Rectangle("Прямоугольник",3,8)
print(rec.name, "\n", "Площадь:", rec.area(), "\n")

cir = Circle("Круг",6)
print(cir.name, "\n", "Площадь:", cir.area(), "\n")

rh = Rhombus("Ромб",5, 6)
print(rh.name, "\n", "Площадь:", rh.area(), "\n")
