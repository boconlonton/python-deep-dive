# Goal 1: Polygon class
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
        return self._edges

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

    def __repr__(self):
        """Customize the object's instance representation"""
        return f'Polygon(no_of_edges={self.edges}, ' \
               f'no_of_vertices={self.vertices}, ' \
               f'circumradius={self.cradius})'

    def __eq__(self, other):
        """Definition of equality"""
        if isinstance(other, Polygon):
            return self.edges == other.edges and self.cradius == other.cradius
        else:
            return NotImplemented

    def __gt__(self, other):
        """Definition of greater than"""
        if isinstance(other, Polygon):
            return self.edges > other.edges
        else:
            return NotImplemented


# Usage
p1 = Polygon(no_of_edges=4, cradius=3)
p2 = Polygon(no_of_edges=4, cradius=3)
p3 = Polygon(no_of_edges=3, cradius=3)

print(p1)
print(p1.vertices)
print(p1.edges)
print(p1.cradius)
print(p1.interior_angle)
print(p1.edge_length)
print(p1.apothem)
print(p1.area)
print(p1.perimeter)
print(p1 == p2)
print(p1 is p2)
print(p1 > p3)
