"""Property Decorator"""

p = property(lambda self: print('getting property'))


def my_decorator(fn):
    print('decorating function')

    def inner(*args, **kwargs):
        print('running decorated function')
        return fn(*args, **kwargs)
    return inner


def undecorated_function(a, b):
    print('running original function')
    return a + b


undecorated_function = my_decorator(undecorated_function)
undecorated_function(1, 2)


@my_decorator
def my_func(a, b):
    print('running original function')
    return a + b


my_func(1, 2)


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        # This will be the docstring of property name
        """The Person's name"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # name = property(name)
    # name = name_temp.setter(name)


def get_prop(self):
    print('getter called')


def set_prop(self, value):
    print('setter called')


def del_prop(self):
    print('deleter called')


p = property(get_prop)
p1 = p.setter(set_prop)
print(p1 is p)  # False
print(p1.fget is p.fget)

p = property(get_prop)
p = p.setter(set_prop)


class Person:
    name = p


person = Person()
person.name = 'Hello'
person.name
