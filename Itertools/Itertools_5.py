import itertools as it

"""
    Let's see some more of the itertools functions.

    iterools.product(*iterable, repeat=1)
        Cartesian product of inputs iterables. Equivalent of the nested for loops.

"""

print(list(it.product([1,2, 3], ['a','b'])))

"""
    itertools.tee(iterable, n=2)
        Create any number of independent iterators from a single input iterable.
"""
iter1, iter2 = it.tee([1,2,3], 2)
print(list(iter1))
print(list(iter2))

"""
    itertools.islice(iterable, start, stop, step)
        Return an iterator whose __next__() method returns selected values from an iterable.
        Works like a slice() on a list but returns an iterator.
"""

print(list(it.islice([1, 2, 3, 4, 5], 3)))
print(list(it.islice([1, 2, 3, 4, 5], 1,3)))

"""
    itertools.chain(*iterables)
        Returns a chain object whose __next__() method returns elements from the first iterable
        until it is exhausted, then elements from the next iterable, until all of the iterables
        are exhausted.
"""
print(list(it.chain('abc', [1,2,3])))