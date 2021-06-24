"""Slots & Single Inheritance"""


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    pass


s = Student('Alex')
print(s.__dict__)


class Person:
    __slots__ = 'name',

    def __init__(self, name):
        self.name = name


class Student(Person):
    pass


s = Student('Eric')
print(s.__dict__)


class Person:
    __slots__ = 'name'

    def __init__(self, name):
        self.name = name


class Student(Person):
    __slots__ = 'school', 'student_number'

    def __init__(self, name, school, studen_number):
        super().__init__(name)
        self.school = school
        self.student_number = studen_number


s = Student('James Bond', 'MI6 PREP', '007')


class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):
    __slots__ = 'school', 'student_number'

    def __init__(self, name, school, studen_number):
        super().__init__(name)
        self.school = school
        self.student_number = studen_number


s = Student('James Bond', 'MI6 PREP', '007')
print(s.__dict__)


# Combining slots & instance dictionary
class Person:
    __slots__ = 'name', '__dict__'

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('Alex', 19)
print(p.__dict__)

