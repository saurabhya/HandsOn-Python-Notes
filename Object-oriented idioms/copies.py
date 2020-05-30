"""
    The easiest way to copy a list (or most immutable collections) is to use the built-in constructor of the type itself.

"""
l1 = [3,[55,44], (7,8,9)]
l2 = list(l1)
print(l2)
print(l1 == l2)
print(l1 is l2)

"""
    For lists and other mutable sequences, the shortcut l2 = l1[:] also makes a copy.
    However, using the constructor or [:] produces a shallow copy (i.e., the outermost container is duplicated,
    but the copy is filed with references to the same items held by the original conatainer). This saves memory
    and causes no probles if all the items are immutable. but if there are mutable items, this may lead to unpleasent
    surprises.
"""
l1 = [3,[66, 55, 44], (7, 8, 9)]
l2 = list(l1)
l1.append(100)
l1[1].remove(55)
print('l1: ', l1)
print('l2: ', l2)
l2[1] += [33,22]
l2[2] += (10,11)
print('l1: ', l1)
print('l2: ', l2)


"""
    It should be clear by now that shallow copies are easy to make, but they may or may not be what you want. How to
    make deep copies?

    Working with shallow copies are not always a problem, but sometimes you need to make deep copies (i.e., dupicates
    that do not share references to embedded objects). the copy module provides the deepcopy and copy functions that
    return deep and shallow copies of arbitrary objects.
"""

class Bus:
    def __init__(self, passengers = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

"""
    Now we will crete a bus object (bus1) and two clones - a shallow copy(bus2) and a deep copy (bus3) - to observe
    what happens as bus1 drops off a student.
"""

import copy
bus1 = Bus(['Alice', 'Bill','Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 =copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))
bus1.drop('Bill')
print(bus2.passengers)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
print(bus3.passengers)

"""
    Note that making deep copies is not a simple matter in the general case. Objects may have cyclic references that
    would cause a naive algorithm to enter an infinte loop. The deepcopy function remembers the objects already copied
    to handle cyclic references garcefully.
"""

a = [10,20]
b = [a,30]
a.append(b)
print(a)


from copy import deepcopy
c = deepcopy(a)
print(c)

"""
    Also, a deep copy may br too deep in some ccases. For example, objects may refer to external resources or singletons that
    should not be copied. ou can control the behavior of both copy and deepcopy by implementing __copy__() and __deepcopy__()
    special methods as in copy module.
"""