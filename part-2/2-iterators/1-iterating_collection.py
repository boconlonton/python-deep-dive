"""
Concept of Iterating through a iterables:
    - Simply define next() method
Issues:
    - Can NOT iterate by for loop, comprehension
    - Can NOT restart => the iterator, once complete loop => exhausted
"""


class Square:

    def __init__(self, length):
        self.i = 0
        self.length = length

    def __next__(self):
        """Overloaded built-in next() function"""
        if self.i > self.length:
            raise StopIteration
        else:
            self.i += 1
            return self.i ** 2


# Usage
sq = Square(5)
while True:
    try:
        print(next(sq))
    except StopIteration:
        break
