"""Creating Dictionaries"""
import itertools
import math


# Example: Grid
x_coordinates = (-2, -1, 0, 1, 2)
y_coordinates = (-2, -1, 0, 1, 2)

grid = (
    (x, y)
    for y in y_coordinates
    for x in x_coordinates
)
grid = itertools.product(x_coordinates, y_coordinates)
grid_extended = {
    (x, y): math.hypot(x, y)
    for x, y in grid
}

# Using dict.fromkeys(iterable, value)
counters = dict.fromkeys('abc', 0)
print(counters)
