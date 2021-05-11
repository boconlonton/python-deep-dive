"""Yielding and Generators"""
import math


class FactIter:
    """Factorial iterator"""

    def __init__(self, n):
        self._n = n
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= self._n:
            raise StopIteration
        else:
            result = math.factorial(self._i)
            self._i += 1
        return result


# Usage
fact_iter = FactIter(5)
print(list(fact_iter))


def my_func():
    print('line 1')
    yield 'FLying'
    print('line 2')
    yield 'Circus'


f = my_func()  # Generator factory
# Generator is an iterator (Iterator Protocol)
print(type(f))
print('__iter__' in dir(f))  # True
print('__next__' in dir(f))  # True
print(iter(f) is f)  # True

# Usage
print(f.__next__())  # Pause at 1st yield
print(f.__next__())  # Pause at 2nd yield


def silly():
    yield 'Hello'
    yield 'Python'
    yield 'I'
    yield 'am'
    if True:
        # Return not show on yield
        # After return is message of StopIteration exception
        return 'Sorry, Its done'
    yield 'Mr.'
    yield 'Generator'


# Usage
gen = silly()
for c in gen:
    print(c)


# Rewrite FactIter
def fact(n):
    for i in range(n):
        yield math.factorial(i)


def squares(n):
    for i in range(n):
        yield i**2


# Usage
gen = fact(5)
for res in gen:
    print(res)
