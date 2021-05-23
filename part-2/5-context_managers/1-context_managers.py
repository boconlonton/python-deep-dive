"""Create a custom context manager"""


class MyContext:
    def __init__(self):
        self.obj = None

    def __enter__(self):
        print('entering context...')
        self.obj = 'the Return object'
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting context...')
        if exc_type:
            print(f'*** Error occured: {exc_type}, {exc_val}')
        return True


# Usage
ctx = MyContext()
print('created context...')
with ctx as obj:
    print('inside with block')
    raise ValueError('custom message')
# with MyContext() as obj:
#     print('inside with block')
#     raise ValueError('custom message')
print(obj)


class File:
    """Mimic the file manager of Python"""
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print('opening file...')
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('closing file...')
        self.file.close()
        return False
