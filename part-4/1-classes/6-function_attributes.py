class Person:
    def say_hello():
        print('Hello')


p = Person()
print(p.say_hello)  # bound method <=> Method
print(type(p.say_hello))  # method
print(type(Person.say_hello))  # function


class Person:
    def say_hello(*args):
        print('say_hello args: ', args)


print(Person.say_hello())
p = Person()
print(p.say_hello())  # the object is injected as first param


class Person:
    def set_name(instance_obj, new_name):
        instance_obj.name = new_name


p = Person()
p.set_name('John')
Person.set_name(p, 'Alex')


class Person:
    def say_hello(self):
        print(f'{self} says hello')


p = Person()
p.say_hello()
m = p.say_hello
print(m.__func__)
print(hex(id(p)))
print(m.__self__)  # reference points to p


class Person:
    def say_hello(self):
        print(f'instance method called from {self}')


p = Person()
p.say_hello()
Person.do_work = lambda self: print(f'do work called from {self}')

print(p.say_hello)
print(p.do_work)
