"""Custom Immutable Sequence Type which supports:
    - __len__()
    - __getitem__()
        + Negative indices
        + Slice object
"""

from functools import lru_cache


class Fib:
    """A custom sequence type of Fibonacci number"""

    def __init__(self, n):
        """Define constructor"""
        self.n = n

    def __len__(self):
        """This method defines len()"""
        return self.n

    def __getitem__(self, i):
        if isinstance(i, int):
            if i < 0:
                i = len(self) + i
            if i < 0 or i > len(self):
                raise IndexError
            else:
                return Fib._fib(i)
        elif isinstance(i, slice):
            # idx_tuple = i.indices(len(self))
            # start, stop, step = idx_tuple
            # rng = range(start, stop, step) = range(*idx_tuple)
            # return [Fib._fib(i) for i in rng)

            return [self.__getitem__(item) for item in range(*i.indices(len(self)))]

    @staticmethod
    @lru_cache(2 ** 10)
    def _fib(n):
        if n < 2:
            return 1
        else:
            return Fib._fib(n - 1) + Fib._fib(n - 2)


# Usage
fib = Fib(10)
print(list(fib))
print(fib[0])
print(fib[-1])
print(fib[0:5])
print(fib.__getitem__(slice(0, 5)))
