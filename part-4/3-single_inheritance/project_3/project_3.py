class Resource:
    __slots__ = '_name', '_manufacturer', '_total', '_allocated', '__dict__'

    def __init__(self, name, manufacturer, total, *, allocated=0):
        self._name = name
        self._manufacturer = manufacturer
        self._total = self.validate_numeric(total)
        self._allocated = self.validate_numeric(allocated)

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    @property
    def category(self):
        return self.__class__.__name__.lower()

    def check_availability(self, *, died=False):
        if died:
            return self._allocated in range(1, self._total + 1)
        else:
            return self._allocated < self._total

    def claim(self, value):
        value = self.validate_numeric(value, greater_than_zero=True)
        if self.check_availability and value <= (self._total - self._allocated):
            self._allocated += value
        else:
            raise ValueError(f'Not enough {self.__class__.__name__}')

    def freeup(self, value):
        value = self.validate_numeric(value, greater_than_zero=True)
        if value <= self._allocated:
            self._allocated -= value
        else:
            raise ValueError(f'Freeup value bigger than Allocated')

    def died(self, value):
        value = self.validate_numeric(value)
        if self.check_availability(died=True) and value <= self._allocated:
            self._allocated -= value
            self._total -= value
        else:
            raise ValueError(f'Cannot implement this action. Please check total & allocated.')

    def purchased(self, value):
        value = self.validate_numeric(value)
        self._total += value

    @staticmethod
    def validate_numeric(value, *, greater_than_zero=False):
        if isinstance(value, int):
            if greater_than_zero and value > 0:
                return value
            elif value >= 0:
                return value
        raise ValueError('Value must be an integer and greater than 0')

    def __str__(self):
        return f'{self.__class__.__name__}(name={self._name})'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}, ' \
               f'manufacturer={self.manufacturer}, ' \
               f'total={self.total}, ' \
               f'allocated={self.allocated})'


class CPU(Resource):

    def __init__(self, name, total, manufacturer,
                 cores, socket, power_watts, *, allocated=0):
        super().__init__(name, manufacturer, total, allocated=allocated)
        self._cores = self.validate_numeric(cores)
        self._socket = socket
        self._power_watts = self.validate_numeric(power_watts)

    @property
    def core(self):
        return self._cores

    @property
    def socket(self):
        return self._socket

    @property
    def power_watts(self):
        return self._power_watts


class Storage:
    __slots__ = '_capacity_gb', '__dict__'

    def __init__(self, capacity_gb):
        self._capacity_gb = Resource.validate_numeric(capacity_gb)

    @property
    def capacity_gb(self):
        return self._capacity_gb


class SSD(Storage):

    def __init__(self, capacity_gb, interface):
        super().__init__(capacity_gb)
        self._interface = interface

    @property
    def interface(self):
        return self._interface


class HDD(Storage):

    def __init__(self, size, rpm, capacity_gb):
        super().__init__(capacity_gb)
        self._size = Resource.validate_numeric(size)
        self._rpm = Resource.validate_numeric(rpm)

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm
