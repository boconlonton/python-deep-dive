"""Goal 2: Polygon sequence type"""

from math import sin, cos, pi
from fractions import Fraction
from numbers import Number
import math


class Polygon:
    """Polygon class"""

    def __init__(self, no_of_edges, cradius):
        self._edges = no_of_edges
        self._vertices = no_of_edges
        self._cradius = cradius
        self._interior_angle = None
        self._edge_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None
        self._efficiency_ratio = None

    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, no_of_edges):
        if isinstance(no_of_edges, int) and no_of_edges > 0:
            self._edges = no_of_edges
            self._interior_angle = None
            self._edge_length = None
            self._apothem = None
            self._area = None
            self._perimeter = None
            self._efficiency_ratio = None

        else:
            raise ValueError('No of edges must be Positive Integer')

    @property
    def cradius(self):
        return self._cradius

    @cradius.setter
    def cradius(self, cradius):
        if isinstance(cradius, Number) and cradius > 0:
            self._cradius = cradius
            self._interior_angle = None
            self._edge_length = None
            self._apothem = None
            self._area = None
            self._perimeter = None
            self._efficiency_ratio = None
        else:
            raise ValueError('Circumradius must be number and greater than 0')

    @property
    def interior_angle(self):
        """Calculate the polygon's interior angles"""
        if not self._interior_angle:
            self._interior_angle = (self.edges - 2)*180/self.edges
        return self._interior_angle

    @property
    def edge_length(self):
        """Calculate the polygon's edges length"""
        if not self._edge_length:
            self._edge_length = 2 * self.cradius * sin(pi/self.edges)
        return self._edge_length

    @property
    def apothem(self):
        """Calculate the polygon's apothem"""
        if not self._apothem:
            self._apothem = self.cradius * cos(pi/self.edges)
        return self._apothem

    @property
    def area(self):
        """Calculate the polygon's area"""
        if not self._area:
            print('lazy_load')
            self._area = Fraction(1, 2) \
                * self.edges \
                * self.edge_length \
                * self.apothem
        return self._area

    @property
    def perimeter(self):
        """Calculate the polygon's perimeter"""
        if not self._perimeter:
            self._perimeter = self.edges * self.edge_length
        return self._perimeter

    @property
    def efficiency_ratio(self):
        """Calculate area/perimeter ratio"""
        if not self._efficiency_ratio:
            self._efficiency_ratio = self.area/self.perimeter
        return self._efficiency_ratio

    def __repr__(self):
        """Customize the object's instance representation"""
        return f'Polygon(no_of_edges={self._edges}, ' \
               f'no_of_vertices={self._vertices}, ' \
               f'circumradius={self._cradius})'

    def __eq__(self, other):
        """Definition of equality"""
        # if isinstance(other, Polygon)
        if isinstance(other, self.__class__):
            return self.edges == other.edges \
                   and self.cradius == other.cradius
        else:
            return NotImplemented

    def __gt__(self, other):
        """Definition of greater than"""
        if isinstance(other, self.__class__):
            return self.edges > other.edges
        else:
            return NotImplemented


class PolygonIterable:
    """Polygon Sequence Type"""

    def __init__(self, largest_vertices, common_cradius):
        self.edges = largest_vertices
        self.vertices = largest_vertices
        self.cradius = common_cradius
        self._max_efficiency = None

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, largest_vertices):
        if largest_vertices >= 3:
            self._edges = largest_vertices
        else:
            raise ValueError('Largest must be greater than or equal 3')

    @property
    def max_efficiency(self):
        """Return the highest efficiency polygon"""
        if not self._max_efficiency:
            efficiency_polygons = sorted(iter(self),
                                         key=lambda pol: pol.efficiency_ratio)
            self._max_efficiency = efficiency_polygons[-1]
        return self._max_efficiency

    def __getitem__(self, s):
        """Definition of instance[]"""
        return list(iter(self))[s]

    def __iter__(self):
        return self.PolygonIterator(self.vertices, self.cradius)

    class PolygonIterator:
        """
        Define Polygon Iterator which implements Iterator Protocol:
            - __iter__ return self
            - __next__ return next()
        """
        def __init__(self, largest_vertices, common_cradius):
            self.largest_vertices = largest_vertices
            self.common_cradius = common_cradius
            self.i = 3

        def __len__(self):
            """Definition of len()"""
            return self.largest_vertices - 2

        def __iter__(self):
            return self

        def __next__(self):
            if self.i > self.largest_vertices:
                raise StopIteration
            else:
                result = Polygon(self.i, self.common_cradius)
                self.i += 1
                return result


def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001

    n = 3
    R = 1
    p = Polygon(n, R)
    assert p.vertices == n, (f'actual: {p.vertices},'
                                   f' expected: {n}')
    assert p.edges == n, f'actual: {p.edges}, expected: {n}'
    assert p.cradius == R, f'actual: {p.cradius}, expected: {n}'
    assert p.interior_angle == 60, (f'actual: {p.interior_angle},'
                                    ' expected: 60')
    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
    assert math.isclose(p.area, 2,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')

    assert math.isclose(p.edge_length, math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.edge_length},'
                                           f' expected: {math.sqrt(2)}')

    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           f' expected: {4 * math.sqrt(2)}')

    assert math.isclose(p.apothem, 0.707,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           ' expected: 0.707')
    p = Polygon(6, 2)
    assert math.isclose(p.edge_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)

    p = Polygon(12, 3)
    assert math.isclose(p.edge_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)

    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5


# Usage
# ps = PolygonSequence(largest_vertices=10, common_cradius=2)
p = Polygon(4, 2)
polygon_iter = PolygonIterable(8, 3)
for p in polygon_iter:
    print(p)
print(polygon_iter.max_efficiency)

# test_polygon()
