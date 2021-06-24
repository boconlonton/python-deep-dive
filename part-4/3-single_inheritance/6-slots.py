"""Slots"""


class Location:
    __slots__ = 'name', '_longtitude', '_latitude'

    def __init__(self, name, *, lon, lat):
        self._longtitude = lon
        self._latitude = lat
        self.name = name

    @property
    def longtitude(self):
        return self._longtitude

    @property
    def latitude(self):
        return self._latitude


Location.map_service = 'Google Maps'
l = Location('Mumbai', lon=19.0760, lat=106.1235)
print(l.name, l.longtitude, l.latitude)
# l.map_link = 'https://'  # Can NOT add attribute
del l.name
del l._longtitude
del l._latitude
