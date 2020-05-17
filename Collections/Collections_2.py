"""
    Collections.OrderdDict()
        The order of keys in Python dictionories is arbitrary, they are not governed by the order in which you add them.
"""
d = {'foo': 5, 'bar': 6}
print(d)
d['baz'] = 7
print(d)
d['foobar'] = 8
print(d)

"""
    The arbitrary orderning implies that you may get different results with the above code.

    The order in which the keys appear is the order which they would be iterated.

    The collections.Orderdict class provides dictionary objects that retain the order of keys. OrderedDict can be created as shown below
    with a series of ordered items.
"""
from collections import OrderedDict

d = OrderedDict([('foo', 5), ('bar', 6)])
print(d)
d['baz'] = 7
print(d)
# Or we can simply create an empty OrderedDict and then add items
"""
    Iterating through an OrderedDict allows Key access in the order thwy were added

    What happens if we assign a new value to an existing key?
"""
d['foo'] = 4
print(d)