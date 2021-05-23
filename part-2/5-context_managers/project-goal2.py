"""
Create a context manager using generator function
"""
from contextlib import contextmanager
import csv
from collections import namedtuple


@contextmanager
def file_parse(fname):
    f = open(fname, 'r')
    try:
        dialect = csv.Sniffer().sniff(f.read(10))
        f.seek(0)
        datas = csv.reader(f, dialect)
        headers = map(lambda s: s.lower(), next(datas))
        nt = namedtuple('Record', list(headers))
        yield (nt(*data) for data in datas)
    finally:
        f.close()


with file_parse('materials/personal_info.csv') as f:
    for data in f:
        print(data)
