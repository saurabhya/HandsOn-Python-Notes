"""
    Python 3.4 does not have any infix operator for the dot product.
    However the later version 3.5 and so on has @ the sign available for
    that purpose.
    The @ operator is supported by the special methods __matmul__, __rmatmul__
    and __imatmul__, named for "matrix multiplication".
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

    def __matmul__(self, other):
        try:
            return sum(a*b for a,b in zip(self, other))
        except TypeError:
            return NotImplemented

    def __rmatmul__(self, other):
        return self@other


# Demonstration of dot product

va = Vector([1,2,3])
vz = Vector([5,6,7])
print(va@vz)