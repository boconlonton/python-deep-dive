"""Iterating callables"""
import random


def counter():
    i = 0

    def inc():
        nonlocal i
        i += 1
        return i
    return inc


class CallableIterator:
    def __init__(self, callable_, sentinel):
        self.callable = callable_
        self.sentinel = sentinel
        self.is_consumed = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_consumed:
            # Exhaust the callable after consumed
            raise StopIteration
        else:
            result = self.callable()
            if result == self.sentinel:
                self.is_consumed = True
                raise StopIteration
            else:
                return result


# Usage
cnt = counter()
cnt_iter = CallableIterator(cnt, 5)
for c in cnt_iter:
    print(c)

# Usage with iter()
cnt = counter()
cnt_iter = iter(cnt, 5)
for c in cnt_iter:
    print(c)

# Create an iterator for random function
# which will stop when meet sentinel

random_iter = iter(lambda:
                   random.randint(0, 10), 8)
random.seed(0)
for num in random_iter:
    print(num)


def countdown(start=10):
    def run():
        nonlocal start
        start -= 1
        return start
    return run


print('---------')
takeoff = countdown(10)
takeoff_iter = iter(takeoff, -1)
for num in takeoff_iter:
    print(num)
