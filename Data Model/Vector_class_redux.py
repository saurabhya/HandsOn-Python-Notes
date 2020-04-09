"""
    Every object oriented language has at least one standard way of getting a string representation from any object.
    Python has two :
    repr():
        Return a string representing the object as the developer wants to see it.

    str():
        Return a string representing the object as the user wants to see it.

    As you know, we implemented the special methods __repr__ and __str__ to support repr() and str().
    There are two additional methods to support alternative representations of objects: __bytes__ and __format__.
    the __bytes__ method is analogous to __str__: it's called by bytes() to get the object rerpresented as a byte
    sequence. Regarding __format__, both the built-in function format() and the str.format() method call it to get
    string displays of objects using special formatting codes. We'll cover __bytes__ in the next example, and __format__
    after that.

    We will try to implement vector2D class to incorporate different functionalities that a mathematical vector can do.
"""

from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))
"""
    Method _eq_ works for vector2d operands but also returns True when comparing vector2d instnaces to other
    iteratables holding the same numeric values (e.g. vector(3,4) == [3,4]).
"""