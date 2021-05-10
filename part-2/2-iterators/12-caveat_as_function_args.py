"""
Caveat of using iterators as Function Arguments
"""
import random


class Randoms:

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            self.i += 1
            return random.randint(0, 100)
