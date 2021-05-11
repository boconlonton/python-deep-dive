"""
Example: Fibonacci sequence
Fib(0) = 1
Fib(1) = 1

Fib(n) = Fib(n-1) + Fib(n-2)
"""


def fib_recursive(n):
    if n <= 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


# Usage with list_comprehension
lst_fib = [fib_recursive(i) for i in range(7)]
print(lst_fib)


def fib_non_recursive(n):
    fib_1 = 1
    fib_2 = 1
    fib_n = 1
    for i in range(n-1):
        # My way
        # fib_n = fib_2 + fib_1
        # fib_1, fib_2 = fib_2, fib_n
        # Fred way
        fib_1, fib_2 = fib_2, fib_2 + fib_1
    return fib_2


lst_fib = [fib_non_recursive(i) for i in range(7)]
print(lst_fib)


# Create FibIter
class FibIter:
    """Fib Iterator"""

    def __init__(self, n):
        self._n = n
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= self._n:
            raise StopIteration
        else:
            result = fib_non_recursive(self._i)
            self._i += 1
            return result


# Usage
fib_iter = FibIter(7)
lst_fib = [fib for fib in fib_iter]
print(lst_fib)


# Refactor fib_non_rec into a generator
def fib_gen(n):
    fib_1 = 1
    yield fib_1
    fib_2 = 1
    yield fib_2
    for i in range(n-2):
        fib_1, fib_2 = fib_2, fib_2 + fib_1
        yield fib_2


# Usage
gen = fib_gen(7)
lst_fib = [fib for fib in gen]
print(lst_fib)
