"""
Project: Implement some concepts in Modular Arithmetic
"""
from functools import total_ordering
import operator


@total_ordering
class Mod:
    def __init__(self, value, modulus):
        self.validate_number_int(value)
        self.validate_number_int(modulus)
        self._modulus = modulus
        self._value = value % modulus

    @property
    def value(self):
        return self._value

    @property
    def modulus(self):
        return self._modulus

    @staticmethod
    def validate_number_int(value):
        if isinstance(value, int):
            return True
        raise ValueError('value must be an integer')

    def _validate_compatile(self, other):
        if isinstance(other, int):
            other = Mod(other, self.modulus)
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return other
        raise TypeError('Incompatible types')

    def __add__(self, other):
        other = self._validate_compatile(other)
        return Mod(self.value + other.value, self.modulus)

    def __iadd__(self, other):
        other = self._validate_compatile(other)
        self._value += other.value
        return self

    def __sub__(self, other):
        other = self._validate_compatile(other)
        return Mod(self.value - other.value, self.modulus)

    def __isub__(self, other):
        other = self._validate_compatile(other)
        self._value -= other.value
        return self

    def __mul__(self, other):
        other = self._validate_compatile(other)
        return Mod(self.value * other.value, self.modulus)

    def __imul__(self, other):
        other = self._validate_compatile(other)
        self._value *= other.value
        return self

    def __pow__(self, other):
        other = self._validate_compatile(other)
        return Mod(self.value ** other.value, self.modulus)

    def __ipow__(self, other):
        other = self._validate_compatile(other)
        self._value **= other.value
        return self

    def __lt__(self, other):
        other = self._validate_compatile(other)
        return self.value < other.value

    def __eq__(self, other):
        other = self._validate_compatile(other)
        return self.value == other.value

    def __hash__(self):
        return hash((self.value, self.modulus))

    def __int__(self):
        return self.value

    def __repr__(self):
        return f'Mod(value={self.value}, modulus={self.modulus})'
