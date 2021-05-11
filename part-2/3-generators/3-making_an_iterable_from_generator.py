"""Making an Iterable from a Generator"""


class Squares:
    """An iterable that return square result"""

    def __init__(self, n):
        self._n = n

    def __iter__(self):
        """Iterable Protocol"""
        return Squares.squares_gen(self._n)

    @staticmethod
    def squares_gen(n):
        """A generator that return result of n**2"""
        for i in range(n):
            yield i ** 2


# Usage
sq = Squares(5)
for num in sq:
    print(num)
print(list(sq))
