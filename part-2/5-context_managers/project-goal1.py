"""
Create a context manager that:
- input: file_name
_ outpur: a lazy iterator that iterate over the data file and yield the named tuple
"""
import csv
from collections import namedtuple


def get_dialect(fname):
    with open(fname, 'r') as f:
        sample = f.read(10)
        dialect = csv.Sniffer().sniff(sample)
    return dialect


class DataIterator:
    def __init__(self, fname):
        self._fname = fname
        self._f = None
        self._nt = None
        self._data = None

    def __iter__(self):
        """Iterator protocol"""
        return self

    def __next__(self):
        if self._f.closed:
            raise StopIteration
        else:
            return self._nt(*next(self._data))

    def __enter__(self):
        """Context Manager protocol"""
        self._f = open(self._fname, 'r')
        self._data = csv.reader(self._f, get_dialect(self._fname))
        headers = map(lambda s: s.lower(), next(self._data))
        self._nt = namedtuple('Record', headers)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        self._f.close()
        return False


with DataIterator('materials/cars.csv') as f:
    print(next(f))
