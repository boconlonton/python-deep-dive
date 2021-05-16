"""Zipping"""
from itertools import zip_longest


# RECAPS: zip(*iterables) - based on shortest iterable
def integer(n):
    for i in range(n):
        yield i


def squares(n):
    for i in range(n):
        yield i**2


def cubes(n):
    for i in range(n):
        yield i**3


# Usage
iter1 = integer(6)
iter2 = squares(5)
iter3 = cubes(4)
# Exhausted at iter3 since it is the shortest
print(list(zip(iter1, iter2, iter3)))

# itertools.zip_longest()
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4]
l3 = [1, 2, 3]
# Based on l1 - longest iterable
# Fill the gap with 'N/A'
print(list(zip_longest(l1, l2, l3, fillvalue='N/A')))
