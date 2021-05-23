"""Generators & Context Manager"""


# def my_gen():
#     try:
#         print('creating & yielding')
#         yield [1, 2, 3, 4]
#     finally:
#         print('exiting context & cleaning up')
def my_gen():
    try:
        print('creating & yielding')
        yield [1, 2, 3, 4]
    finally:
        print('exiting context & cleaning up')


gen = my_gen()
lst = next(gen)
print(lst)
try:
    next(gen)
except StopIteration:
    pass


class GenCtxManager:
    def __init__(self, gen_func, *args, **kwargs):
        self._gen = gen_func(*args, **kwargs)

    def __enter__(self):
        return next(self._gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False


with GenCtxManager(my_gen) as obj:
    print(obj)
