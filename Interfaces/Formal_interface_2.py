"""
    Once you've imported the abc module, you can directly register a virtual subclass
    by using the .register() metamethod. Now, we register the interface Double as a virtual
    base class of the built-in __float__ class:
"""
import abc

class Double(metaclass = abc.ABCMeta):
    """Double precisio floating point number """
    pass

Double.register(float)
# You can check the effect of using .register():
print(issubclass(float,Double))
print(isinstance(1.2345, Double))

"""
    By using the .register() meta method, you've successfully registered Double as a Virtual
    subclass of float.

    Once you've have registered Double, you ca use it as class decorator to set
    the decorated class as a virtual subclass.
"""
@Double.register
class Double64:
    """A 64-bit double-precision floating-point number."""
    pass

print(issubclass(Double64, Double))
# The decorated rediter method helps you to create a heirarchy of custom
# virtual class inheritance.