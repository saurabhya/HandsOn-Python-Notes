"""
    We will overload * operator for scaler multiplication for now.
    Another kind of product involving Vector operands would be dot product
    of two vectors - or matrix mutiplication, if you take one vector as
    1*N matrix and the other as N*1 matrix. The current practice in NumPy
    and similar libraries is not to overload the* with these two meanings,
    but to use * only for the scalar product.

    Back to our scalar product, again we start with the simplest __mul__
    and __rmul__ methods.
"""

from array import array
import reprlib
import math
import itertools
import numbers

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
        return Vector(a+b for a, b in pairs)
    def __radd__(self, other):
        return self+other

    # Overloading * operator
    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(n*scalar for n in self)
        else:
            return NotImplemented
    def __rmul__(self, other):
        return self*other
    """
        These methods do work, except when provided with incompatible operands.
        The scalar argument has to be a number that when multiplied by a float
        produces another float. So a complex number will not do, but the scalar
        can be an int, a bool(because bool is a subclass of int) or even
        a fractions.Fraction instance.

        We could the duck typing and catch a TypeError in __mul__, but there is
        another, more explicit way that make sense in this situation: goose typing.

        We use isinstance() to check the type of scalar, but instead of hardcoding
        some concrete types, we check against numbers.Real ABC, which covers all
        the types we need, and keeps our implementation open to future numeric types
        that declare themselves actual and virtual subcalsses of the number.Real ABC.
    """



# Demonstration of overloading
v1 = Vector([1,2,3])
print(v1*3)
print(3*v1)