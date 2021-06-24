"""
Single Inheritance
"""


class Shape:
    pass


class Ellipse(Shape):
    pass


class Circle(Ellipse):
    pass


class Polygon(Shape):
    pass


class Rectangle(Polygon):
    pass


class Square(Rectangle):
    pass


class Triangle(Polygon):
    pass


# issubclass
print(issubclass(Ellipse, Shape))  # True
print(issubclass(Circle, Shape))  # True

print(issubclass(Polygon, Ellipse))  # False
print(issubclass(Square, Shape))  # True


s = Shape()
e = Circle()
sq = Square()

print(isinstance(s, Shape))  # True
print(isinstance(sq, Rectangle))  # True
print(isinstance(sq, Shape))  # True

print(type(Shape))
print(type(s))

sq = Square()
p = Polygon()

print(isinstance(sq, type(p)))
