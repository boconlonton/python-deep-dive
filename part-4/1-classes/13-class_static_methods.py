from datetime import datetime, timezone, timedelta
from time import sleep


class Person:
    def hello(arg='default'):
        """Bound method"""
        print(f'Hello, with arg={arg}')


class MyClass:
    def hello():
        print('hello...')

    def instance_hello(arg):
        print(f'hello from {arg}')

    @classmethod
    def class_hello(arg):
        print(f'hello from {arg}')


m = MyClass()
MyClass.hello()
# m.hello()  # Not work
m.instance_hello()
m.class_hello()  # passing the class as the first argument
MyClass.class_hello()

print(MyClass.class_hello)
print(MyClass.instance_hello)
print(MyClass.hello)


# Usage of @staticmethod
class MyClass:
    def hello():
        print('hello...')

    def instance_hello(arg):
        print(f'hello from {arg}')

    @classmethod
    def class_hello(arg):
        print(f'hello from {arg}')

    @staticmethod
    def static_hello():
        print('Static method called')


m = MyClass()
m.static_hello()  # Worked since it is static method


# Use case
class Timer:
    tz = timezone.utc

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)

    @staticmethod
    def current_dt_utc():
        return datetime.now(timezone.utc)

    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)


Timer.set_tz(-7, 'MST')
print(Timer.tz)

t1 = Timer()
t2 = Timer()

print(t1.tz, t2.tz)
Timer.set_tz(-8, 'PST')
print(t1.tz, t2.tz)


t = Timer()
print(t.current_dt_utc())
print(Timer.current_dt_utc())

print(Timer.current_dt_utc(), Timer.current_dt())

t1 = Timer()
t2 = Timer()


class TimerError(Exception):
    """A custom exception used for Timer class"""


class Timer:
    tz = timezone.utc  # This will affect all instances of this class

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)

    @staticmethod
    def current_dt_utc():
        return datetime.now(timezone.utc)

    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)

    def start(self):
        """An instance method"""
        self._time_start = self.current_dt_utc()
        self._time_end = None

    def stop(self):
        if self._time_start is None:
            raise TimerError('Timer must be started before it can be stopped')
        self._time_end = self.current_dt_utc()

    @property
    def start_time(self):
        if self._time_start is None:
            raise TimerError('Timer has not been started')
        return self._time_start.astimezone(self.tz)

    @property
    def end_time(self):
        if self._time_end is None:
            raise TimerError('Timer has not been stopped')
        return self._time_end.astimezone(self.tz)

    @property
    def elapsed(self):
        if self._time_start is None:
            raise TimerError('Timer must be started')
        if self._time_end is None:
            elapsed_time = self.current_dt_utc() - self._time_start
        else:
            elapsed_time = self._time_end - self._time_start
        return elapsed_time.total_seconds()


t1 = Timer()
t1.start()
sleep(2)
t1.stop()
print(f'Start time: {t1.start_time}')
print(f'End time: {t1.end_time}')
print(f'Elasped: {t1.elapsed:.2f} seconds')

t2 = Timer()
t2.start()
sleep(3)
t2.stop()
print(f'Start time: {t2.start_time}')
print(f'End time: {t2.end_time}')
print(f'Elasped: {t2.elapsed:.2f} seconds')

Timer.set_tz(-7, 'MST')
print(f'Start time: {t1.start_time}')
print(f'End time: {t1.end_time}')
print(f'Elasped: {t1.elapsed:.2f} seconds')
