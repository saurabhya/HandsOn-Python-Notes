def better_grouper(inputs, n):
    iters = [iter(inputs)]*n
    return zip(*iters)

"""
    The problem with better_grouper() is that it doesn't handle situations where the value passed
    to the second argument isn't a factor of the length of the iterable in the first argument:
"""


nums = [1,2,3,4,5,6,7,8,9,10]
print(list(better_grouper(nums, 4)))

"""
    The elements 9 and 10 are missing from the grouped output. This happens because zip() stops
    aggregating elements once the shortest iterable passed to it is exhausted. It would make more
    sense to return a third group containing 9 and 10.

    To do this, you can itertools.zip_longest(). This function accepts any number of iterables as arguments
    and a fillvalue keyword argument that defaults to None. The easiest way to get a sense of the difference
    between zip() and zip_longest() is to look at some example output:
"""

import itertools as it

x = [1,2,3,4,5]
y = ['a', 'b', 'c']
print(list(zip(x, y)))
print(list(it.zip_longest(x,y)))