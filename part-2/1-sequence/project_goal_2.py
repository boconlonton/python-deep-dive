"""Goal 2: Polygon sequence type"""

from math import sin, cos, pi
from fractions import Fraction
from numbers import Number


class Polygon:
    """Polygon class"""

    def __init__(self, no_of_edges, cradius):
        self.edges = no_of_edges
        self.vertices = no_of_edges
        self.cradius = cradius

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, no_of_edges):
        if isinstance(no_of_edges, int) and no_of_edges > 0:
            self._edges = no_of_edges
        else:
            raise ValueError('No of edges must be Positive Integer')

    @property
    def cradius(self):
        return self._cradius

    @cradius.setter
    def cradius(self, cradius):
        if isinstance(cradius, Number) and cradius > 0:
            self._cradius = cradius
        else:
            raise ValueError('Circumradius must be number and greater than 0')

    @property
    def interior_angle(self):
        """Calculate the polygon's interior angles"""
        return (self.edges - 2)*(100/self.edges)

    @property
    def edge_length(self):
        """Calculate the polygon's edges length"""
        return 2 * self.cradius * sin(pi/self.edges)

    @property
    def apothem(self):
        """Calculate the polygon's apothem"""
        return self.cradius * cos(pi/self.edges)

    @property
    def area(self):
        """Calculate the polygon's area"""
        return Fraction(1, 2) \
            * self.edges \
            * self.edge_length \
            * self.apothem

    @property
    def perimeter(self):
        """Calculate the polygon's perimeter"""
        return self.edges * self.edge_length

    @property
    def efficiency_ratio(self):
        """Calculate area/perimeter ratio"""
        return self.area/self.perimeter

    def __repr__(self):
        """Customize the object's instance representation"""
        return f'Polygon(no_of_edges={self.edges}, ' \
               f'no_of_vertices={self.vertices}, ' \
               f'circumradius={self.cradius})'

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


class PolygonSequence:
    """Polygon Sequence Type"""

    def __init__(self, largest_vertices, common_cradius):
        self.edges = largest_vertices
        self.vertices = largest_vertices
        self.cradius = common_cradius
        self.polygons = [
            Polygon(no_of_edges=vertices, cradius=common_cradius)
            for vertices in range(3, largest_vertices+1)
        ]

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
        efficiency_polygons = sorted(self.polygons,
                                     key=lambda pol: pol.efficiency_ratio)
        return efficiency_polygons[-1]

    def __getitem__(self, s):
        """Definition of instance[]"""
        return self.polygons[s]

    def __len__(self):
        """Definition of len()"""
        return len(self.polygons) - 2


# Usage
ps = PolygonSequence(largest_vertices=10, common_cradius=2)
print(len(ps))
print(ps.max_efficiency)
print(ps[2])
for p in ps:
    print(p)
