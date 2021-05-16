"""Selecting & Filtering iterators"""
from itertools import filterfalse, takewhile, dropwhile, compress
from math import sin, pi


def gen_cubes(n):
    for i in range(n):
        print(f'yielding {i}')
        yield i**3


def is_odd(x):
    return x % 2 == 1


def sine_wave(n):
    start = 0
    max_ = 2 * pi
    step = (max_ - start)/(n-1)

    for _ in range(n):
        yield round(sin(start), 2)
        start += step


filtered = filter(is_odd, gen_cubes(10))
print(list(filtered))

# itertools.filterfalse
filtered_false = filterfalse(is_odd, gen_cubes(10))
print(list(filtered_false))

# itertools.takewhile: Stop iterate at where the predicate turns False
takewhile_ex = takewhile(lambda x: 0 <= x <= 0.9, sine_wave(15))
print(list(sine_wave(15)))
print(list(takewhile_ex))

# itertools.dropwhile: Begin to iterate at where the predicate turns False
l = [1, 3, 5, 2, 1]
dropwhile_ex = dropwhile(lambda x: x < 5, l)
print(list(dropwhile_ex))

# itertools.compress()
data = ['a', 'b', 'c', 'd', 'e']
selectors = [True, False, 1, 0]  # None
print(list(zip(data, selectors)))
# How compress works
print([item for item, truth_value in zip(data, selectors) if truth_value])
compress_ex = compress(data, selectors)
print(list(compress_ex))
