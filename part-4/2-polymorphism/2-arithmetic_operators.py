from numbers import Real
from math import sqrt


class VectorDimensionMismatch(TypeError):
    pass


class Vector:
    def __init__(self, *components):
        if len(components) < 1:
            raise ValueError('Cannot create an empty Vector')
        for component in components:
            if not isinstance(component, Real):
                raise ValueError(f'Vector components must all be real numbers. {component} is invalid')

        self._components = tuple(components)

    @property
    def components(self):
        return self._components

    def __len__(self):
        return len(self._components)

    def __repr__(self):
        return f'Vector{self.components}'

    def __add__(self, other):
        """
        Define a + b
        """
        if not self.validate_type_and_dimension(other):
            # raise VectorDimensionMismatch('Vectors must be same dimension')
            return NotImplemented
        components = (x + y for x, y in zip(self.components, other.components))
        return Vector(*components)

    def __sub__(self, other):
        """
        Define a - b
        """
        if not self.validate_type_and_dimension(other):
            # raise VectorDimensionMismatch('Vectors must be same dimension')
            return NotImplemented
        components = (x - y for x, y in zip(self.components, other.components))
        return Vector(*components)

    def __mul__(self, other):
        """
        Define a * x => x is a number
        """
        print('__mul__ called...')
        if isinstance(other, Real):
            components = (other * x for x in self.components)
            return Vector(*components)
        elif self.validate_type_and_dimension(other):
            """dot product"""
            components = (x * y for x, y in zip(self.components, other.components))
            return sum(components)
        else:
            return NotImplemented

    def __rmul__(self, other):
        """
        Define x * a
        """
        print('__rmul__ called...')
        return self * other

    def __matmul__(self, other):
        print('__matmul__ called')

    def __iadd__(self, other):
        if self.validate_type_and_dimension(other):
            components = (x + y for x, y in zip(self.components, other.components))
            self._components = tuple(components)
            return self  # Mutation
            # return self + other  # Not mutation
        else:
            return NotImplemented

    def __neg__(self):
        print('__neg__ called')
        components = (-x for x in self.components)
        return Vector(*components)

    def __abs__(self):
        print('__abs__ called...')
        return sqrt(sum(x**2 for x in self.components))

    def validate_type_and_dimension(self, v):
        return isinstance(v, Vector) and len(v) == len(self)


v1 = Vector(1, 2)
v2 = Vector(10, 20)
v3 = Vector(4, 5, 6, 7)
print(v1 + v2)
print(v1 * 10)
print(v1.__mul__(10))
print('-----REFLECTED OPERATOR----')
print(10 * v1)  # __rmul__
print(v1.__rmul__(10))
print(v1 * v2)  # Dot product
print(v1 @ v2)  # __matmul__
print('-----IN-PLACE OPERATOR----')
print(id(v1))
v1 += v2  # __iadd__
print(v1, id(v1))
print('-----UNARY OPERATOR----')
v1 = Vector(1, 2)
v2 = Vector(10, 20)
print(-v1)  # __neg__
print(v1 + -v2)
print('-----abs()----')
print(abs(v1))  # __abs__
# print(v1 + v3)  # VectorMismatch exception


# Arithmetic Operator Polymorphism is NOT just for numeric
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person('{self.name}')"


p1 = Person('John')


class Family:
    def __init__(self, mother, father):
        self.mother = mother
        self.father = father
        self.children = []

    def __iadd__(self, other):
        self.children.append(other)
        return self


f = Family(Person('Mary'), Person('John'))
f += Person('Eric')
print(f.children)
