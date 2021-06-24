class Person:
    pass


p = Person()

print(bool(p))  # Always True since no __len__, no __bool__


class MyList:
    def __init__(self, length):
        self._length = length

    def __len__(self):
        print('__len__ called')
        return self._length


l1 = MyList(0)
l2 = MyList(10)

print(bool(l1), bool(l2))


class MyList:
    def __init__(self, length):
        self._length = length

    def __len__(self):
        print('__len__ called ...')
        return self._length

    def __bool__(self):
        print('__bool__ called...')
        return self._length > 0


l1 = MyList(0)
l2 = MyList(10)

print(bool(l1), bool(l2))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        # return self.x != 0 or self.y != 0
        return bool(self.x or self.y)
        # return self.x or self.y  # NOT WORKED since return value must be boolean


p1 = Point(0, 0)
p2 = Point(1, 1)

print(bool(p1), bool(p2))
print(bool(p1.x or p1.y))
