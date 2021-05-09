"""
Iterables vs Iterator
- Iterables is an object implements the iterable protocol
    + __iter__ => return the iterator
- Iterator is an object implements the iterator protocol
    + __iter__ => return itself
    + __next__ => return next item or StopIteration
- This solves the exhaustion problem
"""


class Cities:
    """Handling the iterable protocol"""

    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'London']

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        return self.CityIterator(self)

    def __getitem__(self, s):
        return self._cities[s]

    class CityIterator:
        """Handling the iterator protocol"""

        def __init__(self, city_object):
            self._index = 0
            self._city_object = city_object

        def __iter__(self):
            return self

        def __next__(self):
            if self._index >= len(self._city_object):
                raise StopIteration
            else:
                item = self._city_object._cities[self._index]
                self._index += 1
                return item


# Usage
cities = Cities()
for city in cities:
    print(city)
for city in cities:
    print(city)
