"""Additional Uses"""
import decimal
from time import perf_counter, sleep
import sys


# Use case 1: Change-Reset
class precision:
    def __init__(self, prec):
        self.prec = prec
        self.current_prec = decimal.getcontext().prec

    def __enter__(self):
        decimal.getcontext().prec = self.prec

    def __exit__(self, exc_type, exc_val, exc_tb):
        decimal.getcontext().prec = self.current_prec
        return False


with precision(3):
    print(decimal.Decimal(1) / decimal.Decimal(3))
print(decimal.Decimal(1) / decimal.Decimal(3))
with decimal.localcontext() as ctx:
    ctx.prec = 3
    print(decimal.Decimal(1) / decimal.Decimal(3))
print(decimal.Decimal(1) / decimal.Decimal(3))


# Use case 2: Start-Stop
class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.stop = perf_counter()
        self.elapsed = self.stop - self.start
        return False


with Timer() as timer:
    sleep(1)
print(timer.elapsed)


# Use case 3: Redirect
class OutToFile:
    def __init__(self, fname):
        self._fname = fname
        self._current_stdout = sys.stdout

    def __enter__(self):
        self._file = open(self._fname, 'w')
        sys.stdout = self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self._current_stdout
        self._file.close()
        return False


with OutToFile('test.txt'):
    print('Line 1')
    print('Line 2')
print('Line 1')


# Use case 4: Wakky Puffy
class Tag:
    def __init__(self, tag):
        self._tag = tag

    def __enter__(self):
        print(f'<{self._tag}>', end='')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'</{self._tag}>', end='')
        return False


with Tag('p'):
    print('some ', end='')
    with Tag('b'):
        print('bold', end='')
    print(' text', end='')


# Use case 5:
print()


class ListMaker:
    def __init__(self, title, prefix='- ', indent=3):
        self._title = title
        self._prefix = prefix
        self._indent = indent
        self._current_indent = 0
        print(title)

    def __enter__(self):
        self._current_indent += self._indent
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._current_indent -= self._indent
        return False

    def print_item(self, arg):
        s = ' ' * self._current_indent + self._prefix + str(arg)
        print(s)


with ListMaker('Items') as lm:
    lm.print_item('Item 1')
    with lm:
        lm.print_item('sub item 1a')
        lm.print_item('sub item 1b')
    lm.print_item('Item 2')
