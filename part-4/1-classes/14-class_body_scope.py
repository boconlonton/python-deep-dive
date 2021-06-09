class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 4

    @property
    def version(self):
        return '{}.{}.{}'.format(
            self.MINOR,
            self.MAJOR,
            self.REVISION
        )

    @classmethod
    def cls_version(cls):
        return '{}.{}.{}'.format(
            cls.MINOR,
            cls.MAJOR,
            cls.REVISION
        )

    @staticmethod
    def static_version():
        return '{}.{}.{}'.format(
            Language.MINOR,
            Language.MAJOR,
            Language.REVISION
        )


class Language2:
    MAJOR = 3
    MINOR = 7
    REVISION = 4


def full_version():
    return '{}.{}.{}'.format(
        Language.MAJOR,
        Language.MINOR,
        Language.REVISION
    )


class Language2:
    MAJOR = 3
    MINOR = 7
    REVISION = 4

    version = full_version


# The function itself is in the global scope => not worked
# class LanguageBAD:
#     MAJOR = 3
#     MINOR = 7
#     REVISION = 4
#
#     def version(self):
#         return '{}.{}.{}'.format(MAJOR, MINOR, REVISION)


print(Language2.version())


MAJOR = 0
MINOR = 0
REVISION = 1


def gen_class():
    MAJOR = 0
    MINOR = 4
    REVISION = 2

    class Language:
        MAJOR = 3
        MINOR = 7
        REVISION = 4

        @classmethod
        def version(cls):
            return '{}.{}.{}'.format(MAJOR, MINOR, REVISION)


name = 'Guido'


class MyClass:
    name = 'Raymond'
    list_1 = [name] * 3
    list_2 = [name for i in range(3)]

    @classmethod
    def hello(cls):
        return '{} says hello'.format(name)


print(MyClass.hello())  # Guido - since this is a closure
print(MyClass.list_1)  # Raymond - since it is a list with a local scope
print(MyClass.list_2)  # Guido - since comprehension is a function => closure
