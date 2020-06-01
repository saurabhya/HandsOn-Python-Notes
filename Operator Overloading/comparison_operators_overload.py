"""
    The handling of the rich comparison operators ++, !=, >, <, <=, >=
    by the Python interpreter is similar to what we just saw, but differs
    in two important aspects:
    1. The same set of methods are used in forward and reverse operator calls.
       For example, in the case of ==, both the forward and reverse calls invoke
       __eq__, only swapping arguments; and a forward call to __gt__ is followed
       by a reverse call to __lt__ with the swapped arguments.
    2. In the case of == ad !=, if the reverse call fails, Python compares the
       object IDs instead of raising TypeError.
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

    def __len__(self):
        return sum(1 for _ in self)

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
    # Overloading == operator.
    def __eq__(self, other):
        if isinstance(other, Vector):
            return (len(self) == len(other) and all(a == b for a, b in zip(self, other)))
        else:
            return NotImplemented
    """
        t3 = (1,2,3)
        va == t3 # true
        is probably not desirable. I really have no hard rule about this;
        it depends on the application context.
        Taking a clue from Python itself, we can see that [1,2] == (1,2)
        is False. Therfore, let's be conservative and do some type checking.
        If the second operand is a vector instance, then use the same logic as the current __eq__.
        Otherwise, return NotImplemented and let Python handle that.

        How about !=? we don't need to implement it because the fallback behavior of the __ne__
        inherited from object suits us: when __eq__ is defined and does not return NotImplemented,
        __ne__ returns that result negated.
    """
    def __ne__(self, other):
        eq_result = self == other
        if eq_result is NotImplemented:
            return NotImplemented
        else:
            return not eq_result



# examples of == operator
va = Vector([1.0, 2.0, 3.0])
vb = Vector(range(1, 4))
print(va == vb)
print(vb == va)
t3 = (1, 2, 3)
print(va == t3)
print(va != t3)