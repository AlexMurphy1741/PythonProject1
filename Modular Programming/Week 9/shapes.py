class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        area = self.width * self.height
        return area

    def circumference(self):
        addition = self.width + self.height
        circumference = addition * 2
        return circumference

    def __str__(self):
        return f"A rectangle of {self.width} by {self.height} = Circumference {self.circumference()}, Area {self.area()}"

    def main(width, height):
       return Rectangle(width, height)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        import math
        twopi = math.pi * 2
        cirmumference = twopi * self.radius
        return cirmumference


    def area(self):
        import math
        rsquared = self.radius ** 2
        area = math.pi * rsquared
        return area


    def __str__(self):
        return f"A circle of radius {self.radius} has a circumference of {self.circumference():,.2f} and an area of {self.area():,.2f}"

    def main(radius):
       return Circle(radius)

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        area = self.side * self.side
        return area

    def circumference(self):
        circumference = self.side * 4
        return circumference

    def __str__(self):
        return f"A square of length {self.side} has a circumference of {self.circumference()} and an area of {self.area()}"

    def main(side):
       return Square(side)

class Cylinder:
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def surface_area(self):
        import math
        twopi = math.pi * 2
        radius_height = self.height * self.radius
        surface_area = twopi * radius_height
        return surface_area

    def __str__(self):
        return f"A cylinder of height {self.height} and radius {self.radius} has a surface area of {self.surface_area():,.2f}"

    def main(width, radius):
       return Cylinder(width, radius)

# def main():
#     x = Rectangle(5, 6)
#     print(x)
#     y = Circle(5)
#     print(y)
#     z = Square(8)
#     print(z)
#     a = Cylinder(9, 5)
#     print(a)