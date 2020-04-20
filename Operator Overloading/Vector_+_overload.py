"""
    Here we will perform addition of two euclidean vectors that will result in a new ector in which
    the components are the pairwise additions of the components of the addends.
"""
from array import array
import reprlib
import math
import itertools


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    # Implementing operator overloading
    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    # Overloading + operator
    def __add__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue =0.0)
        # Pairs is a generator that will produce tuples(a, b) where a is from self and b is from other.
        # If self and other have different lengths then fillvalue will supply the missing values for the
        # shorter iterable
        return Vector(a+b for a, b in pairs)
    """
    However if we try to swap the operands, the mixed type addition fails
    v1 = Vector([3,4,5])
    (10,20,30)+ v1 # TypeError: can only concatenate tuple (not "Vector") to tuple

    The __radd__() method is called the "reflected" or "reversed" version of __add__().
    Some call them "reversed" special methods, they are called on the righthand operand.
    Whatever "r" word you prefer, that's what the "r" prefix stands for in __radd__(), __rsub__() etc.

    Therfore, to make the mixed type addition work, we need to implement the Vector.__radd__ method,
    which Python will invoke as a fall back if the left operand does not implement __add__ or
    if it does but returns NotImplemented to signal that it doesn't know how to handle
    the right operand.
    """
    def __radd__(self, other):
        return self+other

# Examples of vector addition:
v1 = Vector([3,4,5])
print(v1+(10, 20, 30))
print(v1+ (10, 20))

# after implementation of __radd__
v1 = Vector([3,4,5])
print((10,20,30)+ v1)