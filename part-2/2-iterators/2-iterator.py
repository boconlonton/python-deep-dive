"""
An object is called Iterator if it implement the following methods:
    - __iter__(): return the object itself
    - __next__(): return the next item or raise StopIteration
Issues:
    - Exhaustion problems!
"""


class Squares:

    def __init__(self, length):
        self.length = length
        self.i = 0

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i **2
            self.i += 1
            return result

    def __iter__(self):
        """Defines the iterator protocol"""
        return self


# Usage
sq = Squares(5)
for item in sq:
    print(item)

# Usage with comprehension
sq = Squares(5)
lst = [(item, item+1) for item in sq]
print(lst)

# Usage with enumerate
sq = Squares(5)
lst = list(enumerate(sq))
print(lst)

# Usage with sorted()
sq = Squares(5)
lst = sorted(sq, reverse=True)
print(list(lst))


class Squares:

    def __init__(self, length):
        self.length = length
        self.i = 0

    def __next__(self):
        print('__next__ called')
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i **2
            self.i += 1
            return result

    def __iter__(self):
        """Defines the iterator protocol"""
        print('__iter__ called')
        return self


# How Python internally iterates an iterator
sq = Squares(5)
for item in sq:
    print(item)

sq = Squares(5)
lst = [item for item in sq if item % 2 == 0]

sq = Squares(5)
sq_iterator = iter(sq)
while True:
    try:
        item = next(sq_iterator)
        print(item)
    except StopIteration:
        break
