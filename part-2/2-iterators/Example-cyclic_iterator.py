"""Cyclic iterators
- 1,2,3,4,5,6,7,8...
- N S W E
=> 1N 2S 3W 4E 5N 6S 7W 8E
"""


class CyclicIterator:

    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        # 1 % 4 = 1
        # 2 % 4 = 2
        # 6 % 4 = 2
        result = self.lst[self.i % len(self.lst)]
        self.i += 1
        return result


# Usage
n = 10
iter_cycl = CyclicIterator('NSWE')
lst = [
    f'{i}{next(iter_cycl)}'
    for i in range(1, n+1)
]
print(lst)

# Usage with zip()
n = 10
iter_cycl = CyclicIterator('NSWE')
lst = [f'{index}{direction}'
       for index, direction in zip(range(1, n+1), iter_cycl)]
print(lst)

# Usage with repetition
lst = [f'{index}{direction}'
       for index, direction in zip(range(1, 11), 'NSWE' * (n // len('NSWE') + 1))]
print(lst)

# Usage with itertools
import itertools

n = 10
iter_cycle = itertools.cycle('NSWE')
items = [f'{index}{next(iter_cycle)}'
         for index in range(1, n+1)]

print(items)


# Another solution
class CyclicIterator2:

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            item = next(self.iterator)
        finally:
            return item


iter_cycle = CyclicIterator2('abc')
for i in range(10):
    print(i, next(iter_cycle))
