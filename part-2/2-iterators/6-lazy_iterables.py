"""Lazy Iterables"""

import math


class Circle:

    def __init__(self, r):
        self.radius = r
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None

    @property
    def area(self):
        if self._area is None:
            print('calculating area...')
            self._area = math.pi + (self.radius ** 2)
        return self._area


# Usage
c = Circle(1)
print(c.radius)
print(c.area)
c.radius = 3
print(c.area)


class Factorials:
    """Lazy Iterables"""

    def __iter__(self):
        return self.FactIter()

    class FactIter:
        def __init__(self):
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            result = math.factorial(self.i)
            self.i += 1
            return result


# Usage
facts = Factorials()
fact_iter = iter(facts)
next(fact_iter)
