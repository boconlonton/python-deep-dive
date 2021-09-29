"""Descriptors"""
from datetime import datetime
from random import choice


class TimeUTC:
    """This is a non-data descriptor"""

    def __get__(self, instance, owner_class):
        print(f'__get__ called, self={self}, '
              f'instance={instance},'
              f'owner_class={owner_class}')
        return datetime.utcnow().isoformat()


class Logger1:
    current_time = TimeUTC()


class Logger2:
    current_time = TimeUTC()


print(Logger1.current_time)
print(Logger2.current_time)

l1 = Logger1()
print(hex(id(l1)))
# Notice on the instance & self
print(l1.current_time)


class TimeUTC1:
    """This is a non-data descriptor"""

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return datetime.utcnow().isoformat()


class Logger3:
    current_time = TimeUTC1()


print(Logger3.current_time)
l3 = Logger3()
print(l3.current_time)


class IntegerValue:
    def __set__(self, instance, value):
        print(f'__set__ called, instance={instance}, value={value}')

    def __get__(self, instance, owner):
        if instance is None:
            print('__get__ called from class')
        else:
            print(f'__get__ called, instance={instance}, owner={owner}')


class Point2D:
    x = IntegerValue()
    y = IntegerValue()


print(Point2D.x)
p = Point2D()
print(p.x)
p.x = 100
print(p.x)
