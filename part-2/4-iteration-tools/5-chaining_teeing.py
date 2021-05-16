"""Chaining & Teeing"""
from itertools import chain, tee

# Chaining
l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

# for gen in l1, l2, l3:
#     for item in gen:
#         print(item)


def chain_iterables(*iterables):
    """Demonstrate how itertools.chain() works"""
    for iterable in iterables:
        yield from iterable


# Usage
l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))
# for item in chain_iterables(l1, l2, l3):
#     print(item)
# Usage with chain()
l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))
# for item in chain(l1, l2, l3):
#     print(item)

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))
lists = [l1, l2, l3]
for item in chain(lists):
    """This simply returns the generator
    NOT iterate over it"""
    print(item)

for item in chain(*lists):
    """This iterate over the returned generator
    BUT it is NOT lazy"""
    print(item)


# Another example
def squares():
    yield (i**2 for i in range(4))
    yield (i**2 for i in range(4, 8))
    yield (i**2 for i in range(8, 12))


for item in chain(*squares()):
    """This iterate over the returned generator
    BUT not lazy"""
    print(item)


# itertools.chain.from_iterable()
c = chain.from_iterable(squares())
for item in c:
    "Lazy evaluation"
    print(item)


def chain_from_iterable(iterable):
    """How chain.from_iterable works"""
    for i in iterable:
        yield from i


# tee()
def squares(n):
    for i in range(n):
        yield i**2


gen = squares(10)
iters = tee(gen, 3)  # Copy into 3 independent iterator
print(iters)
