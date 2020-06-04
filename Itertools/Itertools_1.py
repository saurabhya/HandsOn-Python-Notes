"""
    According to the itertools docs, it is a "module that implements a number of iterator building blocks
    inspired by constructs from APL, Haskell, and SML... Together, they form an 'iteratoralgebra' making it
    possible to construct specialized tools succintly and efficiently in pure Python."

    Looslely speaking, this means that the functions in itertools "operate" on iterators to produce more complex
    iterators. Consider, for example, the built-in zip() function, which takes any number of iterables as
    arguments and returns an iterator over tuples of their corresponding elements.
"""

print(list(zip([1,2,3],['a', 'b', 'c'])))

"""
    The iter() built-in function, when called on an iterables, returns an iterator object for that iterable:
"""
print(iter([1,2,3,4]))

"""
    Under the hood, the zip() function works, in essence, by calling iter() on each of its arguments,
    then advancing each itertor returned by iter() with next() and aggergating into the tuples.
    The iterator returned by zip() iterates over these tuples.

    The map() built-in function is another "itertools operator" that, in its simplest form,
    appliees a single-parameter function to each element of an iterable on element at a time.
"""
print(list(map(len, ['abc', 'de', 'fghi'])))

"""
    The map() function works by calling iter() on its argument, advancing this iterator with next()
    until the iterator is exhausted, and applying the function passed to its first argument to the
    value returned by next() at each step()
"""