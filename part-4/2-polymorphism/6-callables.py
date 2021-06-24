from functools import partial
from collections import defaultdict
from time import perf_counter, sleep
from functools import wraps


class Person:
    def __call__(self):
        print('__call__ called')


p = Person()
p()
print(type(Person))

print(type(partial))


def my_func(a, b, c):
    return a, b, c


partial_func = partial(my_func, 10, 20)

print(partial_func(30))


class Partial:
    def __init__(self, func, *args):
        self._func = func
        self._args = args

    def __call__(self, *args):
        return self._func(*self._args, *args)


partial_func = Partial(my_func, 10, 20)
partial_func(30)

print(callable(print))
print(callable(int))
print(callable(partial_func))

miss_counter = 0


def default_value():
    global miss_counter
    miss_counter += 1
    return 'N/A'


d = defaultdict(default_value)
d['a'] = 1
print(d['b'])
print(miss_counter)


# FAILED
# def default_value(counter):
#     counter += 1
#     return 'N/A'


class DefaultValue:
    def __init__(self):
        self.counter = 0

    def __iadd__(self, other):
        if isinstance(other, int):
            self.counter += other
            return self
        raise ValueError('Can only increment with integer value')

    def __call__(self):
        self.counter += 1
        return 'N/A'


def_1 = DefaultValue()
def_2 = DefaultValue()

cache_1 = defaultdict(def_1)
cache_2 = defaultdict(def_2)

print(cache_1['a'], cache_1['b'])
print(def_1.counter)
print(cache_2['a'])
print(def_2.counter)


class DefaultValue:
    def __init__(self, default_value):
        self.counter = 0
        self.default_value = default_value

    def __iadd__(self, other):
        if isinstance(other, int):
            self.counter += other
            return self
        raise ValueError('Can only increment with integer value')

    def __call__(self):
        self.counter += 1
        return self.default_value


cache_def_1 = DefaultValue(None)
cache_def_2 = DefaultValue(0)

cache_1 = defaultdict(cache_def_1)
print(cache_1['a'])
print(cache_def_1.counter)


# RECAPS: class decorator
# This is BAD since counter is INCORRECT
def profile(fn):
    counter = 0
    total_elapsed = 0
    avg_time = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal counter
        nonlocal total_elapsed
        nonlocal avg_time
        counter += 1
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        total_elapsed += (end - start)
        avg_time = total_elapsed / counter
        return result

    inner.counter = counter
    inner.avg_time = avg_time
    return inner()


def profiler(fn):
    _counter = 0
    _total_elapsed = 0
    _avg_time = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal counter
        nonlocal _total_elapsed
        nonlocal _avg_time
        counter += 1
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        _total_elapsed += (end - start)
        return result

    def counter():
        return _counter

    return inner()


class Profiler:
    def __init__(self, fn):
        self.fn = fn
        self.total_elapsed = 0
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        start = perf_counter()
        result = self.fn(*args, **kwargs)
        end = perf_counter()
        self.total_elapsed += (end - start)
        return result

    @property
    def avg_time(self):
        return self.total_elapsed / self.counter


@Profiler
def func_1(a, b):
    sleep(1)
    return (a, b)


func_1(1, 2)
print(func_1.counter)
print(func_1.total_elapsed)
print(func_1.avg_time)
