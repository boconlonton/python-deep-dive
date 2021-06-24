"""Overriding"""


class Person:
    pass


p = Person()
print(str(p))


class Person:
    def __str__(self):
        return 'Person class'


p = Person()
print(str(p))


class Person:
    def __repr__(self):
        return 'Person() with extra debugging info'


p = Person()
print(str(p))


class Shape:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f'Shape.info called for Shape({self.name})'

    def extended_info(self):
        return f'Shape.extended_info called for Shape({self.name})', self.info()


class Polygon(Shape):
    def __init__(self, name):
        self.name = name

    def info(self):
        return f'Polygon info called for Polygon({self.name})'


p = Polygon('square')
print(p.extended_info())
