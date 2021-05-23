"""Using decorators to create context manager
using generator functions
def gen(args):
    # set up happens here, or inside try
    try:
        yield obj # whatever normally gets returned by __enter__
    finally:
        # perform clean up here
"""
from contextlib import contextmanager, redirect_stdout
from time import perf_counter, sleep
import sys


def open_file(fname, mode='r'):
    print('opening file...')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print('closing file...')
        f.close()


class GenContextManager:
    def __init__(self, gen):
        self.gen = gen

    def __enter__(self):
        print('Calling next to get the yielded value from generator')
        return next(self.gen)

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('Calling next() to clean up the generator')
        try:
            next(self.gen)
        except StopIteration:
            pass
        return False


file_open = open_file('test.txt', 'w')
with GenContextManager(file_open) as f:
    f.writelines('Sir Spamalot')


# Context Manager decorator
def context_manager_dec(gen_fn):
    def helper(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        ctx = GenContextManager(gen)
        return ctx
    return helper


# @context_manager_dec
# def open_file_2(fname, mode='r'):
#     print('opening file...')
#     f = open(fname, mode)
#     try:
#         yield f
#     finally:
#         print('closing file...')
#         f.close()
@contextmanager
def open_file_2(fname, mode='r'):
    print('opening file...')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print('closing file...')
        f.close()


# open_file = context_manager_dec(open_file)
with open_file_2('test.txt', 'r') as f:
    print(f.readlines())


@contextmanager
def timer():
    stats = dict()
    start = perf_counter()
    stats['start'] = start
    try:
        yield stats
    finally:
        end = perf_counter()
        stats['end'] = end
        stats['elapsed'] = end - start


with timer() as stats:
    sleep(2)
print(stats)


@contextmanager
def out_to_file(fname):
    current_stdout = sys.stdout
    file = open(fname, 'w')
    sys.stdout = file
    try:
        yield None
    finally:
        file.close()
        sys.stdout = current_stdout


with out_to_file('test.txt'):
    print('line 1')
    print('line 2')
print('hello')


# Usage of contextlib.redirect_stdout
with open('test.txt', 'w') as f:
    with redirect_stdout(f):
        print('Hello from redirect_stdout')
with open('test.txt', 'r') as f:
    print(f.readlines())
