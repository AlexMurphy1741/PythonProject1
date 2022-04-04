# File used to call the shapes file
import shapes
def object():
    item = input("What is the object: ")
    shape = input("What is the shape of the object(Square, Circle, Cylinder or Square): ")
    return item, shape

def calculations(item, shape):
    if shape == Rectangle:
        height = float(input"What is the height of the object: ")
        width = float(input"What is the width of the object: ")
        return height, width
    elif shape == Circle:

    Elif

from shapes import Rectangle
x = Rectangle.main(5, 6)
print(x)

from shapes import Circle
y = Circle.main(6)
print(y)

from shapes import Square
z = Square.main(5)
print(z)

from shapes import Cylinder
a = Cylinder.main(5, 6)
print(a)