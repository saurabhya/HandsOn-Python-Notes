import itertools as it
"""
    We used itertools.chain() to tack one iterator onto the end of another.
    The chain() function has a class method .from_iterable() that takes a single
    iterable as an argument. The elements of the iterable must themeselves be iterable,
    so th enet effect if that chain.from_iterable() flattens its argument:
"""

print(list(it.chain.from_iterable([[1, 2, 3], [4, 5, 6]])))

"""
    There is no reason th eargument of chain.from_iterable() needs to be finite.
    You could emulate the behavior of itertools.cycle().
"""
cycle = it.chain.from_iterable(it.repeat('abc'))
print(list(it.islice(cycle, 8)))
"""
    The chain.from_iterable90 function is useful when you need to build an iterator over
    data that has been "chunked".
"""