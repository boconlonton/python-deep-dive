from pytz import common_timezones, timezone


LIST_ZONE_NAMES = common_timezones


class TimeZone:
    def __init__(self, name='UTC'):
        self.name = name
        self._data = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value in LIST_ZONE_NAMES:
            self._name = value
            self._data = None
        else:
            raise ValueError('Invalid timezone')

    @property
    def data(self):
        if self._data is None:
            self._data = timezone(self._name)
        return self._data
