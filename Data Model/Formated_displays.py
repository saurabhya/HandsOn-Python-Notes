"""
    The format() built-in function and the str.format() method delegate the actual formatting to each type by calling
    thier .__format()__(for,at_spec) method. The format_spec is a formatting specifier, which is either:
        1. The second argument in format(my_obj, format-spec), or
        2. Whatever appears after the colon in a replacement field delimiited with {} inside a format string used with str.format().

"""

brl = 1/2.43 # BRl to USD currency conversion rate
print(brl)
print(format(brl, '0.4f'))
print('1 BRL = {rate:0.2f} USD'.format(rate = brl))

"""
    The notation used in the formatting specifier is called the Format Specification Mini-Language.

    A few built-in types have their own presentation codes in the Format Specification Mini-language. For example -
    among Several other codes - the int type suuport b and x for base 2 and base 16 output, respectively, while float
    implements f for a fixed-point display and % for a percentage display.
"""
print(format(42, 'b'))
print(format(42, 'x'))
print(format(2/3, '.1%'))

"""
    the formatting specification language is extensible because each class gets to interpret the format_spec argument
    as it likes. For instance, the classes in the datetime module use the same format codes in the strftime() functions
    and in thier __format__ methods.
"""

from datetime import datetime
now = datetime.now()
print(format(now, '%H:%M:%S'))
print("It's now {:%I:%M %p}".format(now))

# If a class has no __format__. the method inherited from object returns str(my_object). because vector2d has a __str__,
# this works:

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


v1 = Vector2d(3,4)
print(format(v1))

"""
    However, if you pass a foramt specifier, object.__format__ raises TypeError
"""
#print(format(v1, '.3f'))

"""
    we will fix this by implementing our own mini-language. The first step will be
    to assume the format specifier provided by the user is intended to format each float component of the vector.
    Implementation is inside vector2d class.
"""
print(format(v1, '.2f'))

"""
    now let's add a custom formatting code to our mini-language: if the format specifier ends with a 'p', we'll display
    the vector in polar coordinates: <r, Θ>, where r is the magnitude and Θ(theta) is the angle in radians.

    To generate polar coordinates we already have the __abs__ method for the magnitude, and we'll code a simple angle
    method using the math.atan2() function to get the angle. Implementation is in the class body
"""
print(format(Vector2d(1,1), '0.5fp'))
print(format(Vector2d(1,1), 'p'))
print(format(Vector2d(1,1), '0.3ep'))

"""
    As we see from here that it is not hard to ectend the format specification mini language to support user-defined types.
"""