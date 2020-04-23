"""
    Any language implementing multiple inheritance needs to deal with potential
    naming conflicts when unrelated acestor classes implement a method by the same name.
    This is called "diamond problem". As done in diamond.py.

    In diamond.py, Note that both classes B and C implement a pong method. The only difference
    is that C.pong outputs the PONG in uppercase.
    If you call d.pong() on an instance of D, which pong method actually runs?
"""

from diamond import *
d = D()

print(d.pong()) # simply calling d.pong() cause the B version to run.
print(C.pong(d)) # You can always call a method on a supercalass directly,
                # passing the instance as an explicit argument.

"""
    The ambiguity of a call like d.pong() is resolved because Python follows a specific
    order when traversing the inheritance graph. That order is called MRO:
    Method Resolution Order. Classes have an attribute called __mro__ holding a tuple of
    references to the superclasses in MRO order, from the current class all the way to
    the object class.
    Let's see what D .__mro__ shows
"""
print(D.__mro__)