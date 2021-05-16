"""Combinatorics"""

import itertools
import fractions


# Cartesian Product
def matrix(n):
    """Generates a square matrix: n x n"""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            yield f'{i} x {j} = {i * j}'


# This result is, essentially, a cartesian product
list(itertools.islice(matrix(10), 10, 20))

l1 = ['x1', 'x2', 'x3', 'x4']
l2 = ['y1', 'y2', 'y3']
for x in l1:
    """How itertools.product works"""
    for y in l2:
        print((x, y), end=' ')
    print(' ')

list(itertools.product(l1, l2))


def matrix(n):
    """Generates a square matrix: n x n"""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            yield i, j, i * j


def matrix_prod(n):
    """Generates a square matrix: n x n
    using itertools.product()"""
    for i, j in itertools.product(range(1, n + 1), range(1, n + 1)):
        yield i, j, i * j


def matrix_prod_tee(n):
    """Generates a square matrix: n x n
    using itertools.product()"""
    iterables = itertools.tee(range(1, n + 1), 2)
    return (
        (i, j, i * j)
        for i, j in itertools.product(*iterables)
    )


# Generate the matrix using itertools.product
# print(list(matrix(5)))
# print(list(matrix_prod(5)))
# print(list(matrix_prod_tee(2)))

# Example 2: Define a grid using cartesian product
def grid(min_val, max_val, step=1, *, num_dimensions=2):
    """Generate a grid of coordinates in 3D"""
    axis = itertools.takewhile(lambda x: x <= max_val,
                               itertools.count(min_val, step))
    axes = itertools.tee(axis, num_dimensions)
    return itertools.product(*axes)


print(list(grid(-1, 1, 0.5)))

# Example 3: Count numbers of eight of a dice
sample_space = list(itertools.product(
    *itertools.tee(range(1, 7), 2)
))
outcomes = list(filter(lambda x: x[0] + x[1] == 8, sample_space))
odds = fractions.Fraction(len(outcomes), len(sample_space))
print(odds)
