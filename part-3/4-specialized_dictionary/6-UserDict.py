"""UserDict"""
from numbers import Real
from collections import UserDict


class IntDict:
    def __init__(self):
        self._d = {}

    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError('Value must be a number')
        else:
            self._d[key] = value

    def __getitem__(self, key):
        return int(self._d[key])


# Improved with usage of get(), dictionary views (inherits from dict)
# Problems: No guarantee that it will use the child method instead of dict method!
# Instead it use the C-compiled method!!!
class IntDict1(dict):
    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError('Value must be a number')
        else:
            super().__setitem__(key, value)

    def __getitem__(self, key):
        return int(super().__getitem__(key))


# Usage of UserDict: Always use the overrided method!!!
class IntDict2(UserDict):
    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError('Value must be a number')
        else:
            super().__setitem__(key, value)

    def __getitem__(self, key):
        return int(super().__getitem__(key))


d = IntDict2()
d['a'] = 10
d['b'] = 100
print(d)
print(d.data)

d1 = IntDict2(a=10, b=3)
d2 = IntDict2({'a': 1.1, 'b': 2.2})
print(d2.values())
print(d2.items())


# Use case
class LimitedDict(UserDict):
    def __init__(self, keyset, min_value, max_value, *args, **kwargs):
        self._keyset = keyset
        self._min_value = min_value
        self._max_value = max_value
        # This will call self.__setitem__ !!!!
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if key not in self._keyset:
            raise KeyError('Invalid key name')
        if not isinstance(value, int):
            raise ValueError('Value must be an integer type')
        if value < self._min_value or value > self._max_value:
            raise ValueError(f'Values must be between {self._min_value} and {self._max_value}')
        super().__setitem__(key, value)

    def __getitem__(self, key):
        return int(super().__getitem__(key))


d = LimitedDict({'red', 'green', 'blue'}, 0, 255, red=10, green=10, blue=10)
print(d)
