'''
    We will implement a class to represent two dimensional vectors - that is euclidean vectors like those
    used in math and physics. We will try to use special metods to provide the simple functionalities
    like additiona and other mathematical operations.
'''
from math import hypot


class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)'%(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x*scalar, self.y*scalar)


'''
    Although we implemented four special methods except __init__, none of them is directly called
    within the class or in the typical usage of the class illustrated by the console listings.
    The Python interpreter is the only frequent caller of the most special methods.

'''