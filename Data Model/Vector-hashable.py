"""
    As we saw in Vector2d implementation that instances are unhashable, so we cannot them in a set:
    v1 =  Vector3d(3, 4)
    hash(v1) -> yields a result.

    To make a Vector2d hashable we must implement __hash__(__eq__ is also required we already implemented it).
    We also need to make vector instances immutable.
    Right now, anyone can do v1.x =7 and there is nothing in the code to suggest that changing a Vector2d is forbidden.
    This is alsothe behavior we want, we'll do that by making the x and y components read-only properties.

"""

class Vector2d:
    typecode = 'd'
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return ( i for i in(self.__x, self.__y))

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

    @classmethod # classmethod decorator
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def angle(self):
        return math.atan2(self.y, self.x) # with this we enhance our __format__ to produce polar coordinates.

    def __format__(self, fmt_spec = ''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    """
        Now that our vectors are reasonably immutable, we can implement the__hash__ method.
        It should return an int and ideally take into account the hashes of the object attibutes that are also used in the __eq__ method,
        because objects that compare equal should have same hash. The __has__ special method documentation suggests using bitwise XOR
        operator(^) to mix the hashes of the components, so that's what we do. The code for our Vector2d.__hash__ method is simply.
    """
    def __hash__(self):
        return hash(self.x)^hash(self.y)


# Let's seee what happens whenwe use hash(v1)
v1 = Vector2d(3,4)
v2 = Vector2d(3.1, 4.2)
print(hash(v1), hash(v2))
print(set([v1, v2]))

"""
    If you are creating a type that has a sensible scalar numeric value, you  may also implement the __int__ and __float__ methods
    invoked by int() and float() constructors which are used for type coercion in som contexts There's also a __complex__ method to
    support complex() built-in constructor.
"""