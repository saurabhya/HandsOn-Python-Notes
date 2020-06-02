"""
    Operator overloading allows user-defined objects to interpolate with infix operators
    such as + and | or unary operator like - and ~. More genrally, function invocation(()),
    attribute access(.), and item access/slicing([]) are also operators in Python but we wil
    only deal with unary and infix operators here.

    Operator overloading has a bad name in some circles. It is a language feature that can be
    abused, resulting in programmer confusion, bugs and unexpected performance bottlenecks.
    But if well used/ it leads to pleasurable APIs and readable code. But in Pythom there are some
    limitations:
    1. We cannot overload operators for built-in types.
    2. We cannot create new operators, only overload existing ones.
    A few operators can't be overloaded: is , and, or, not (but the bitwise &,|,~, can).

    In The Python language Reference, "6.5 Unary arithmetic and bitwise operations" lists
    three unary operators:

    - (__neg__): Arithmetic unary negative. if x -s -2 then -x == 2

    + (__pos__): Arithmetic unary plus. Usually x == +x, but there are few cases where this is not true.

    ~ (__invert__): Bitwise inverse of an integer, defined as ~x == -(x+1). if x is 2 then ~x == -3.

    It's easy to support the unary operators. Simply implement the appropriate special method, which will
    recieve just one argument: self. Use whatever l0gic makes sense in ypur class, but stick o the fundamental
    rule of operators: always rreturn a new object. In other words, do not modify self,
    but create and return a new instance of a suitable type.

    Lets look at the implementation of above mentioned operators in previously mentioned Vector class.
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

    # Implementing operator overloading
    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    """
        We will not implement __invert__, so if the user tries ~v on a vector instanc,
        Pyton will raise TypeError with a clear message: "bad operand type for unary~:'Vector'".
    """
