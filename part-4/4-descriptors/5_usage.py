"""Usage"""
from collections.abc import Sequence


# Example 1

class Int:
    def __set_name__(self, owner, name):
        self.prop_name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'{self.prop_name} must be an integer.')
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)


class Float:
    def __set_name__(self, owner, name):
        self.prop_name = name

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise ValueError(f'{self.prop_name} must be an float.')
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)


class List:
    def __set_name__(self, owner, name):
        self.prop_name = name

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError(f'{self.prop_name} must be a list.')
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)


class Person:
    age = Int()
    height = Float()
    tags = List()
    favourite_foods = List()


p = Person()


# Example 2

class ValidType:

    def __init__(self, type_):
        self._type = type_

    def __set_name__(self, owner, name):
        self.prop_name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise ValueError(f'{self.prop_name} must be of '
                             f'type {self._type.__name__}.')
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)


class Person2:
    age = ValidType(int)
    height = ValidType(float)
    tags = ValidType(list)
    favourite_foods = ValidType(tuple)


# Example 2
'''
Suppose we have a Polygon class that has a vertices property that needs to be
defined as a sequence of Point2D instances. So here, not only do we want the
vertices attribute of our Polygon to be an iterable of some kind, we also want
the elements to all be instances of the Point2D class. In turn, we will also 
want to make sure that coordinates for Point2D are non-negative integer values
'''


class Int3:

    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'{self.name} must be an int.')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'{self.name} must be at least {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'{self.max_value} must be '
                             f'less then {self.max_value}')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.name, None)


class Point2D:
    x = Int3(min_value=0, max_value=800)
    y = Int3(min_value=0, max_value=600)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D(x={self.x}, y={self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'


class Point2DSequence:

    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, Sequence):
            raise ValueError(f'{self.name} must be a sequence type')
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f'{self.name} must contain at least '
                             f'{self.min_length} elements.')
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(f'{self.name} must contain less than '
                             f'{self.max_length} elements.')

        for index, item in enumerate(value):
            if not isinstance(item, Point2D):
                raise ValueError(f'Item at index {index} is '
                                 f'not a Point2D instance')

        instance.__dict__[self.name] = list(value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            if self.name not in instance.__dict__:
                instance.__dict__[self.name] = []
            return instance.__dict__.get(self.name)


class Polygon:

    vertices = Point2DSequence(min_length=3)

    def __init__(self, *vertices):
        self.vertices = vertices

    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instance...')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            raise ValueError(f'Vertices length is at max ({max_length}).')
        self.vertices.append(pt)

    def __len__(self):
        return len(self.vertices)

    def __getitem__(self, idx):
        return self.vertices[idx]

    def __contains__(self, pt):
        return pt in self.vertices


p3 = Polygon(Point2D(0, 0), Point2D(0, 1), Point2D(1, 0))
print(p3.vertices)


class Triangle(Polygon):
    vertices = Point2DSequence(min_length=3, max_length=3)


class Rectangle(Polygon):
    vertices = Point2DSequence(min_length=4, max_length=4)
