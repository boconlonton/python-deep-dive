"""
Polygon exercises:
    - __len__
    - __getitem__ (retrieve)
    - __add__
    - __iadd__
    - __mul__
    - __imul__
    - append()
    - insert()
    - extend()
    - __setitem__ (assignment)
    - __delitem__
"""
import numbers


class Point:
    """"""

    def __init__(self, x, y):
        if isinstance(x, numbers.Real) \
                and isinstance(y, numbers.Real):
            self._pt = (x, y)
        else:
            raise TypeError('Point co-ordinates must be real numbers')

    def __repr__(self):
        return f'Point(x={self._pt[0]}, y={self._pt[1]})'

    # Custom Seq p1
    def __len__(self):
        """Defines len()"""
        return len(self._pt)

    def __getitem__(self, i):
        """Defines obj[i]"""
        return self._pt[i]


class Polygon:

    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        # Removes the square brackets in the result
        pts_str = ",".join(str(pt) for pt in self._pts)
        return f'Polygon({pts_str})'

    # Turn Polygon into a Sequence Type
    def __len__(self):
        """Defines len()"""
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    def __setitem__(self, s, other):
        """Define instance[s] = other"""
        try:
            rhs = [Point(*pt) for pt in other]
            is_single = False
        except TypeError:
            try:
                rhs = Point(*other)
                is_single = True
            except TypeError:
                raise TypeError('Invalid Point or Iterable of Points')
        if isinstance(s, int) and is_single \
                or (isinstance(s, slice) and not is_single):
            # Assignment for a slice
            self._pts[s] = rhs
        else:
            raise TypeError('Incompatible')

    # More methods
    def __add__(self, other):
        """Define p1 + p2"""
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('can only concatenate with same Polygon')

    # def __iadd__(self, other):
    #     """Define p1 += p2
    #     - Mutating
    #     - p2 can be any iterables
    #     """
    #     if isinstance(other, Polygon):
    #         # The memory address of _pts will be changed
    #         points = other._pts
    #     else:
    #         # Modify for more options of right-hand-side
    #         points = [Point(*pt) for pt in other]
    #     self._pts = self._pts + points
    #     return self

    def append(self, pt):
        """Define instance.append()
        NOT need to return
        """
        pt = Point(*pt)
        self._pts.append(pt)

    def insert(self, i, pt):
        """Define instance.insert(i, pt)
        NOT need to return
        """
        self._pts.insert(i, Point(*pt))

    def extend(self, pts):
        """Define instance.extend(pts)
        NOT need to return
        """
        if isinstance(pts, Polygon):
            self._pts += pts._pts
        else:
            self._pts += [Point(*pt) for pt in pts]

    def __iadd__(self, other):
        """Define p1 += p2 (Improved from extend)
        - Mutating
        - p2 can be any iterables
        """
        self.extend(other)
        return self

    def __delitem__(self, s):
        """Define del instance[s]"""
        del self._pts[s]

    def pop(self, s):
        """Define instance.pop(s)"""
        return self._pts.pop(s)

    def clear(self):
        self._pts.clear()


# Usage
p1 = Point(10, 2.5)
print(p1)
x, y = p1
print(x, y)

# This is the beauty of using custom seq over Named Tuple
p2 = Point(*p1)

# Polygon
print('POLYGON')

p = Polygon((0, 0), Point(1, 1))
print(p)
print(p[0])
print(len(p))

print('\n CONCAT POLYGON')
p1 = Polygon((1, 1), (2, 2))
p2 = Polygon((3,3), (4, 4))
result = p1 + p2
print(result)  # New object

print('\n ICONCAT POLYGON')
print(id(p1))
p1 += p2
print(id(p1))  # Original object (Mutating)
print(p1)
print('\n ICONCAT POLYGON (Modified)')
p1 = Polygon((1, 1), (2, 2))
print(id(p1))
p1 += [(0, 0), (6, 2)]
print(id(p1))
print(p1)

print('\n Append')
p1 = Polygon((1, 1), (2, 2))
print(id(p1))
p1.append((3, 4))
print(id(p1))
print(p1)

print('\n Extend')
p1 = Polygon((0, 0), (2, 2))
p2 = Polygon((3, 3), (4, 4))
print(id(p1), p1)
print(id(p2), p2)

p1.append([10, 10])
print(id(p1), p1)

p1.insert(1, Point(-1, -1))
print(id(p1), p1)

p1.extend(p2)
print(id(p1), p1)

p1.extend([(6, 6), Point(20, 20)])
print(id(p1), p1)

print('\n Assignment of slice')
p1 = Polygon((0, 0), (2, 2))
print(id(p1), p1)
p1[0:2] = [(3, 3), Point(20, 20), [30, 30]]
print(id(p1), p1)

print('\n Assignment of value')
p1 = Polygon((0, 0), (2, 2))
print(id(p1), p1)
p1[0] = (3, 3)
print(id(p1), p1)
p1[0] = Point(-1, -1)
print(id(p1), p1)

print('\n Assignment (Modified)')
p1 = Polygon((0, 0), (2, 2))
print(id(p1), p1)
p1[0:2] = [(3, 3), [4,4]]
print(id(p1), p1)

print('\n Del/Pop (Modified)')
p1 = Polygon((0, 0), (2, 2), (3, 3))
print(id(p1), p1)
del p1[0]
print(id(p1), p1)
p1 = Polygon((0, 0), (2, 2), (3, 3))
print(id(p1), p1)
del p1[0:2]
print(id(p1), p1)
p1 = Polygon((0, 0), (2, 2), (3, 3))
print(id(p1), p1)
res = p1.pop(0)
print(res)
print(id(p1), p1)
