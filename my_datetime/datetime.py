from .timezone import TimeZone
from datetime import datetime


class DateTime:
    utc_tz = TimeZone()
    default_fmt = '%Y-%m-%d %H:%M:%S %Z'

    def __init__(self, value, tz):
        self.value = value
        self.tz = tz
        self._data = None
        self._data_utc = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, obj):
        if isinstance(obj, datetime):
            self._value = obj
            self._data = None
            self._data_utc = None
        else:
            raise TypeError('Value must be a datetime object')

    @property
    def tz(self):
        return self._tz

    @tz.setter
    def tz(self, obj):
        if isinstance(obj, TimeZone):
            self._tz = obj
        else:
            if obj:
                raise TypeError('TimeZone must a timezone object')
            else:
                self._tz = TimeZone()
        self._data = None
        self._data_utc = None

    @property
    def local(self):
        if self._data is None:
            self._data = self._tz.data.localize(self._value)
        return self._data

    @property
    def utc(self):
        if self._data_utc is None:
            self._data_utc = self.local.astimezone(self.utc_tz.data)
        return self._data_utc

    @property
    def utc_as_isoformat(self):
        return f'{self.utc.strftime(self.default_fmt)}'

    @property
    def utc_as_string(self):
        return f"{self.utc.strftime('%Y%m%d%H%M%S')}"

    @property
    def local_as_isoformat(self):
        return f'{self.local.strftime(self.default_fmt)} GMT'

    @property
    def local_as_string(self):
        return f"{self.local.strftime('%Y%m%d%H%M%S')}"
