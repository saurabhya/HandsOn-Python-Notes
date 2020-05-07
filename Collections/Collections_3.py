
"""
    collections.defaultdict(default_factory) returns a subclass of dict that has a default value for missing keys. The argument should be a function
    that returns the default value when called woth no arguments. If there is nothing passed, it defaults to None.
"""
import collections
state_capitals = collections.defaultdict(str)
print(state_capitals)

"""
    returns a refernce to a defaultdict that will create a string object with its default_factory method.

    A typical use of defaultdict is to use one of the bulltin types such as str, int or dict as the default_factory, since these
    return empty types when called with no arguments:

    calling the defaultdict with a key that does not produce an error as it would in a normal dictionary.
"""
print(state_capitals['Alaska'])
print(state_capitals)

# Another example with int
fruit_counts = collections.defaultdict(int)

fruit_counts['apple'] += 2 # No errors should occur
print(fruit_counts)

# Normal dictionary methods also work with the defaultdict

# Using list as the default_factory will create a list for each new key

s = [('NC', 'Raleigh'), ('VA', 'Richmond'), ('WA', 'Seattle'), ('NC', 'Asheville')]
dd = collections.defaultdict(list)

for k, v in s:
    dd[k].append(v)
print(dd)