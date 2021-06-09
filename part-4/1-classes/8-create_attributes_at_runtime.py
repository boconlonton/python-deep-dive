from types import MethodType


class Person:
    def __init__(self, name):
        self.name = name


p1 = Person('Eric')
p2 = Person('Alex')


def say_hello(self):
    return f'{self.name} says hello'


print(say_hello(p1))

# Create method at runtime
p1_say_hello = MethodType(say_hello, p1)
p1.say_hello = p1_say_hello
print(p1_say_hello())

# 2nd way
p2.say_hello = MethodType(lambda self: f'{self.name} say Hello too', p2)
print(p2.say_hello())


class Person:
    def __init__(self, name):
        self.name = name

    def register_do_work(self, func):
        setattr(self, '_do_work', MethodType(func, self))

    def do_work(self):
        do_work_method = getattr(self, '_do_work', None)
        if do_work_method:
            return do_work_method()
        else:
            raise AttributeError('You must first register a do work method')


def work_math(self):
    return f'{self.name} will teach differentials today'


math_teacher = Person('Eric')
eng_teacher = Person('John')

math_teacher.register_do_work(work_math)
print(math_teacher.__dict__)
print(math_teacher.do_work())

eng_teacher.register_do_work(lambda self: f'{self.name} will analyze Hamlet today')
print(eng_teacher.do_work())
