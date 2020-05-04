"""
    The built in collections package provides several specialized, flexible collection types that are
    both high performance and provide alternatives to the general collection types of dict, list, tuple
    and set. The module also defines abstract classes describing different types of collection functionality.
"""

# collection.Counter

"""
    Counter is a dict subclass that allows you to easily count objects. It has utility methods for working
    with the frequencies of the objects that you are counting.
"""

import collections
counts = collections.Counter([1, 2, 3])
print(counts)

print(collections.Counter(' Happy Birthday'))
print(collections.Counter('I am sam Sam I am That SA-I-am that'.split()))


c = collections.Counter({'a':4, 'b':2, 'c':-2, 'd':0})
print(c['a'])

# Get the total number of elements in Counter(4+2+0+-2)
#print(sum(c.itervalues())

# Get the elements (only those with positive counter are kept)
print(list(c.elements()))

# Remove keys with 0 or negative values
print(c-collections.Counter())

# remove everything
c.clear()
print(c)

# Add remove individual elements
c.update({'a':3, 'b':3})
c.update({'a':2, 'c':2}) # adds to existing, sets if they don't exist
print(c)

c.subtract({'a':3, 'b':3, 'c':3})
print(c)