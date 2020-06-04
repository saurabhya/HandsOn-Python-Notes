"""
    According to the itertools docs, it is a "module that implements a number of iterator building blocks
    inspired by constructs from APL, Haskell, and SML... Together, they form an 'iteratoralgebra' making it
    possible to construct specialized tools succintly and efficiently in pure Python."

    Looslely speaking, this means that the functions in itertools "operate" on iterators to produce more complex
    iterators. Consider, for example, the built-in zip() function, which takes any number of iterables as
    arguments and returns an iterator over tuples of their corresponding elements.
"""

print(list(zip([1,2,3],['a', 'b', 'c'])))