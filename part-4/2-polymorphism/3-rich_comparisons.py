from math import sqrt
from functools import total_ordering


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        print('__eq__ called...')
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __lt__(self, other):
        print('__lt__ called...')
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return abs(self) < abs(other)

    def __le__(self, other):
        print('__le__ called')
        return self < other or self == other

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'


v1 = Vector(0, 0)
v2 = Vector(0, 0)
v3 = Vector(10, 10)
print(v1 == v2)
print(v1 == (0, 0))
print((0, 0) == v1)

print(v1 < v3)
print(v1 > v3)  # If no __gt__ => called __lt__
print(v1 <= v3)
print(v1 >= v3)


# Usage of @total_ordering
@total_ordering
class Number:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        print('__eq__ called')
        if isinstance(other, Number):
            return self.x == other.x
        return NotImplemented

    def __lt__(self, other):
        print('__lt__ called')
        if isinstance(other, Number):
            return self.x < other.x
        return NotImplemented


a = Number(1)
b = Number(2)
c = Number(1)

print(a == a)
print(a > b)
print(a < c)
print(a >= b)
print(a <= b)
