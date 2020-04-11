"""
    We are goning to create a multi-dimensinal vector class as we did with Vector2d.
    Our strategy to implement Vector will be to use compositic not inheritence. We'll store the components in an array
    of floats, and will implement the methods needed for our Vector to behave like immutable flat sequence.

    But before we implement the sequence methods, let's make sure we have a baseline implementation
    of Vector that is compatible with our Vector2d class.
"""

from array import array
import reprlib
import math

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