"""Nested Context Managers"""
from contextlib import contextmanager, ExitStack


# with open('nested/file1.txt') as f:
#     for row in f:
#         print(row, end='')
# print('\n---------------')
# with open('nested/file2.txt') as f:
#     for row in f:
#         print(row, end='')
# print('\n---------------')
# with open('nested/file3.txt') as f:
#     for row in f:
#         print(row, end='')
# print('---------------')
# with open('nested/file1.txt') as f1, \
#         open('nested/file2.txt') as f2:
#     print(f1.readlines())
#     print(f2.readlines())
# with open('nested/file1.txt') as f1:
#     with open('nested/file2.txt') as f2:
#         with open('nested/file3.txt') as f3:
#             print(f1.readlines())
#             print(f2.readlines())
#             print(f3.readlines())


@contextmanager
def open_file(f_name):
    print(f'opening {f_name}')
    f = open(f_name)
    try:
        yield f
    finally:
        print(f'closing {f_name}')
        f.close()


f_names = 'nested/file1.txt', 'nested/file2.txt', 'nested/file3.txt'

exits = []
enters = []

for f_name in f_names:
    ctx = open_file(f_name)
    enters.append(ctx.__enter__)
    exits.append(ctx.__exit__)

files = [
    enter() for enter in enters
]

while True:
    try:
        rows = [next(f).strip('\n') for f in files]
    except StopIteration:
        break
    else:
        row = ','.join(rows)
        print(row)

for exit in exits[::-1]:
    exit(None, None, None)


# Better solution
class NestedContexts:
    def __init__(self, *contexts):
        self._enters = []
        self._exits = []
        self._values = []

        for ctx in contexts:
            self._enters.append(ctx.__enter__)
            self._exits.append(ctx.__exit__)

    def __enter__(self):
        for enter in self._enters:
            self._values.append(enter())
        return self._values

    def __exit__(self, exc_type, exc_val, exc_tb):
        for exit in self._exits[::-1]:
            exit(exc_type, exc_val, exc_tb)
        return False


with NestedContexts(open_file('nested/file1.txt'),
                    open_file('nested/file2.txt'),
                    open_file('nested/file3.txt')) as files:
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)


# Better Solution: More generics
f_names = 'nested/file1.txt', 'nested/file2.txt', 'nested/file3.txt'
contexts = [open_file(f_name) for fname in f_names]
with NestedContexts(*contexts) as files:
    print('do work')


# Best Solution
class NestedContextsBetter:
    def __init__(self):
        self._exits = []

    def __enter__(self):
        return self

    def enter_context(self, ctx):
        self._exits.append(ctx.__exit__)
        value = ctx.__enter__()
        return value

    def __exit__(self, exc_type, exc_val, exc_tb):
        for exit in self._exits[::-1]:
            exit(exc_type, exc_val, exc_tb)
        return False


with NestedContextsBetter() as stack:
    files = [
        stack.enter_context(open_file(f_name))
        for f_name in f_names
    ]

    print('do work')


# Usage with contextlib.ExitStack
with ExitStack() as stack:
    files = [
        stack.enter_context(open_file(f_name))
        for f_name in f_names
    ]

    print('do work 12')
