"""Delegating to Parent"""
from math import pi
from numbers import Real


class Person:

    def work(self):
        return 'Person works...'


class Student(Person):

    def work(self):
        result = super().work()
        return f'Studen works... and {result}'


s = Student()
print(s.work())


class Person:
    def work(self):
        return 'Person works...'


class Student(Person):
    pass


class PythonStudent(Student):
    def work(self):
        result = super().work()
        return f'PythonStudent codes ... and {result}'


ps = PythonStudent()
print(ps.work())


class Person:
    def work(self):
        return 'Person works...'


class Student(Person):
    def work(self):
        result = super().work()
        return f'Student studies... and {result}'


class PythonStudent(Student):
    def work(self):
        result = super().work()
        return f'PythonStudent codes ... and {result}'


ps = PythonStudent()
print(ps.work())


class Person:
    def work(self):
        return 'Person works...'


class Student(Person):
    def study(self):
        return 'Student studies...'


class PythonStudent(Student):
    def code(self):
        result_1 = self.work()
        result_2 = self.study()
        return f'{result_1} and {result_2} and PythonStudent codes...'


ps = PythonStudent()
print(ps.code())


class Person:
    def work(self):
        return f'{self} works...'


class Student(Person):
    def work(self):
        result = super().work()
        return f'{self} studies... and {result}'


class PythonStudent(Student):
    def work(self):
        result = super().work()
        return f'{self} codes ... and {result}'


ps = PythonStudent()
print(ps.work())


# Use case
class Person:
    def __init__(self, name):
        self.name  = name


class Student(Person):
    def __init__(self, name, student_number):
        super().__init__(name)
        self.student_number = student_number


s = Student('Python', 30)
print(s.__dict__)


# Use case 2
class Circle:
    def __init__(self, r):
        self._set_radius(r)
        # self._r = r
        self._area = None
        self._permiter = None

    @property
    def radius(self):
        return self._r

    # @radius.setter
    # def radius(self, r):
    #     if isinstance(r, Real) and r > 0:
    #         self._r = r
    #         self._area = None
    #         self._permiter = None
    #     else:
    #         raise ValueError('Radius must be a positive real number.')
    def _set_radius(self, r):
        if isinstance(r, Real) and r > 0:
            self._r = r
            self._area = None
            self._permiter = None
        else:
            raise ValueError('Radius must be a positive real number.')

    @radius.setter
    def radius(self, r):
        self._set_radius(r)

    @property
    def area(self):
        if self._area is None:
            self._area = pi * self.radius ** 2
        return self._area

    @property
    def perimeter(self):
        if self._permiter is None:
            self._permiter = 2 * pi * self.radius
        return self._permiter


class UnitCircle(Circle):
    def __init__(self):
        super().__init__(1)

    @property
    def radius(self):
        return super().radius

    @radius.setter
    def radius(self, r):
        return super()._set_radius(r)


u = UnitCircle()
print(u.radius, u.area, u.perimeter)

u.radius = 10
