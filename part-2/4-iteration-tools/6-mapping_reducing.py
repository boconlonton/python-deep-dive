"""Mapping and Reducing"""
from itertools import starmap, accumulate, chain
from functools import reduce
import operator

# Usage of map()
maps = map(lambda x: x**2, range(5))
print(list(maps))


def add(t):
    return t[0] + t[1]


print(list(map(add, [(0, 0), [1, 1], range(2, 4)])))


def add2(x, y):
    return x + y


print(list(add2(*t) for t in [(0, 0), [1, 1], range(2, 4)]))

# Solve the above with starmap()
"""No need to unpacking & also, it is lazy evaluation"""
print(list(starmap(add2, [(0, 0), [1, 1], range(2, 4)])))

# Accumulation: functools.reduce()
# initializer =
print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))


# RECAPS: how reduce() works internally
def mul(x, y):
    return x * y


def reduce_(fn, sq, init=None):
    if init:
        result = init
    else:
        result = sq[0]
    for item in sq[1:]:
        result = fn(result, item)
    return result


sq = [1, 2, 3, 4]
print(reduce_(mul, sq))


# itertools.accumulate()
def running_reduce(fn, iterable, start=None):
    """How itertools.accumulate works internally
    - similar to reduce()
    - BUT yield the intermediate result"""
    it = iter(iterable)
    if start is None:
        acc = next(it)
    else:
        acc = start
    yield acc
    for item in it:
        acc = fn(acc, item)
        yield acc


print(list(running_reduce(lambda x, y: x + y, [10, 20, 30])))
print(list(running_reduce(operator.add, [10, 20, 30])))
# Default fn of accumulate is operator.add
print(list(accumulate([10, 20, 30])))
# Custom fn
print(list(accumulate([10, 20, 30], operator.mul)))
# Start value: accumulate() does NOT support start value
# Work around by using chain()
print(list(accumulate(chain((10,), [10, 20, 30]), operator.mul)))
print(list(running_reduce(operator.mul, [10, 20, 30], 10)))
