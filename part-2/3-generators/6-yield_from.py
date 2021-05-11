"""Yield from"""


def matrix(n):
    gen = (
        (i*j for j in range(1, n+1))
        for i in range(1, n+1)
    )
    return gen


def matrix_iterator(n):
    for row in matrix(n):
        # for item in row:
        #     yield item
        yield from row


# Usage
for item in matrix_iterator(3):
    print(item)
