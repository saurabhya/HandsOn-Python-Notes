"""
    With itertools, you can easily iterators infinte sequences. We will explore numeric sequences,
    but the tools and techniques seen here are by no means limited to numbers.

    Evens and Odds
    We will create a pair of iterators over even and odd integers without explicitly doing any aritmetic.
    Before that let's look at an arithmetic solution using generators.
"""

import itertools as it

def even():
    """ Generate even integers, starting with 0. """
    n = 0
    while True:
        yield n
        n += 2

evens = even()
print(list(next(evens) for _ in range(5)))

def odd():
    n = 1
    while True:
        yield n
        n += 2

odds = odd()
print(list(next(odds) for _ in range(5)))

"""
    That is pretty straight forward, but with itertools you can do this much more compactly.
    The function you need is itertools.count(), which does exactly what it sounds like:
    it counts, starting by default with the number 0.
"""
counter = it.count()
print(list(next(counter) for _ in range(5)))

"""
    You can start counting from any number you like by setting the start keyword argument,
    which defaults to 0. You can even set a step keyword argument to determine the interval
    between numbers returned from count() - this defaults to 1.
    With count(), iterators over even and odd integers become literal one-liners:
"""
evens = it.count(step=2)
print(list(next(evens) for _ in range(5)))

odds = it.count(start= 1, step=2)
print(list(next(odds) for _ in range(5)))

"""
    Ever since Python 3.1, the count() function also accepts non-integer arguments:
"""
count_with_floats = it.count(start= 0.5, step= 0.75)
print(list(next(count_with_floats) for _ in range(5)))

""" You can even pass it negative numbers """
negative_count = it.count(start= -1, step= -0.5)
print(list(next(negative_count) for _ in range(5)))

"""
    In some ways, count() is similar to the built-in range() function, but count() always returns
    an infinite sequence. You might wonder what good an infinte sequence is since it's impossible
    to iterate over completely. That is a valid question, but the following example may be helpful
    in showing what is the importance of infinite sequence which emulates the behavior of the built-in
    enumerate() function.
"""
print(list(zip(it.count(), ['a','b', 'c'])))

"""
    It is a simple example, but think about it: you just enumerated a list without a for loop and without
    knowing the length of the list ahead of time.
"""