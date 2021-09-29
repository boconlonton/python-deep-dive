"""The __set_name__ method"""


class ValidString:

    def __init__(self, min_length):
        self.min_length = min_length

    def __set_name__(self, owner, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a String')
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f'{self.property_name} '
                             f'must be at least {self.min_length} characters')
        key = '_' + self.property_name
        setattr(instance, key, value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        key = '_' + self.property_name
        return getattr(instance, key, None)


class Person:
    first_name = ValidString(min_length=2)
    last_name = ValidString(min_length=3)


p = Person()
p.first_name = 'Tan'
p.last_name = 'Truong'
print(p.first_name, p.last_name)
