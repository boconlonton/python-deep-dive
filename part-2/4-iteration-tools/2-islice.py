"""Slicing"""
import math
from itertools import islice


# Recaps: slicing sequence type
l = [1, 2, 3, 4]
print(l[0:2])
s = slice(0, 2)
print(l[s])


# Slicing an iterator
def factorials(n):
    for i in range(n):
        yield math.factorial(i)


def slice_(iterable, start, stop):
    """Demonstrate how islice() works"""
    for _ in range(0, start):
        next(iterable)

    for _ in range(start, stop):
        yield next(iterable)


facts = factorials(100)
# print(list(slice_(facts, 3, 10)))
# 1st usage way
print(list(islice(factorials(100), 3, 10)))
# 2nd usage way: extended slicing
print(list(islice(factorials(100), 3, 10, 2)))
# islice() returns a lazy iterator
