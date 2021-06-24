"""Extending"""


class Person:
    def routine(self):
        result = self.eat()
        if hasattr(self, 'study'):
            result += self.study()
        result += self.sleep()
        return result

    def eat(self):
        return 'Person eats...'

    def sleep(self):
        return 'Person sleeps...'


class Student(Person):
    def study(self):
        return 'Student studies...'


p = Person()
print(p.routine())

s = Student()
print(s.routine())


# Abstract class
class Account:
    apr = 3.0

    def __init__(self, accout_number, balance):
        self.account_number = accout_number
        self.balance = balance
        self.account_type = 'Generic Account'

    # def calc_interest(self):
    #     return f'Calc interest on {self.account_type} with APR = {type(self).apr}'

    def calc_interest(self):
        return f'Calc interest on {self.account_type} with APR = {self.__class__.apr}'


class Savings(Account):
    apr = 5.0

    def __init__(self, accout_number, balance):
        self.account_number = accout_number
        self.balance = balance
        self.account_type = 'Savings Account'


a = Account(100, 100)
print(a.calc_interest())

s = Savings(100, 100)
print(s.calc_interest())
