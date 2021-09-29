"""Using as Instance properties"""
import weakref


class IntegerValue:
    def __init__(self):
        self.values = weakref.WeakKeyDictionary()

    def __set__(self, instance, value):
        self.values[instance] = int(value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return self.values.get(instance)


class Point:
    x = IntegerValue()


p = Point()
p.x = 100.1
print(p.x)


class IntegerValue2:
    """This solves the problem if the hash-ability of the class
    - However: when delete, the ID is still in the dictionary
    """
    def __init__(self):
        self.values = weakref.WeakKeyDictionary()

    def __set__(self, instance, value):
        self.values[id(instance)] = int(value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return self.values.get(id(instance))


class Point2:
    x = IntegerValue2()


p1 = Point()
p1.x = 100.1
print(p1.x)


class IntegerValue3:
    """This solves the problem if the hash-ability of the class
    & when delete, the ID is still deleted by a callback function
    """
    def __init__(self):
        self.values = {}

    def __set__(self, instance, value):
        self.values[id(instance)] = (weakref.ref(instance, self._remove_object),
                                     int(value))

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return self.values[id(instance)][1]

    def _remove_object(self, weak_ref):
        print(f'remove dead entry for {weak_ref}')
        reverse_lookup = [key for key, value in self.values.items()
                          if value[0] is weak_ref]
        if reverse_lookup:
            key = reverse_lookup[0]
            del self.values[key]


class Point3:
    x = IntegerValue3()


p3 = Point3()
p3.x = 100.1
print(p3.x)
del p3
print(Point3.x.values)


class ValidString:

    def __init__(self, min_length=0, max_length=255):
        self.data = {}
        self._min_length = min_length
        self._max_length = max_length

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('Value must be a string')
        if len(value) < self._min_length:
            raise ValueError(f'Value should be at least '
                             f'{self._min_length} chars')
        if len(value) > self._max_length:
            raise ValueError(f'Value cannot exceed {self._max_length} chars')
        self.data[id(instance)] = (weakref.ref(instance,
                                               self._finalize_instance),
                                   value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value_tuple = self.data.get(id(instance))
            return value_tuple[1]

    def _finalize_instance(self, weak_ref):
        reverse_lookup = [key for key, value in self.data.items()
                          if value[0] is weak_ref]
        if reverse_lookup:
            key = reverse_lookup[0]
            del self.data[key]


class Person:
    first_name = ValidString(5, 255)
    last_name = ValidString(5, 255)

    def __eq__(self, other):
        return isinstance(other, Person) and self.first_name == other.first_name


p1 = Person()
p1.first_name = 'Tancdasc'
print(p1.first_name)
