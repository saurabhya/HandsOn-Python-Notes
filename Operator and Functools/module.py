"""
    Often in functional programming it is convenient to use an arithmetic operator as a function. For example,
    suppose you want to multiply a sequence of numbers to calculate factorial without using recursion. To perform
    summations, you can use sum, but there is no equivalent function for multiplication. you could use reduce -
    but this requires to multiply two items of the sequence.
"""

from functools import reduce

def fact1(n):
    return reduce(lambda a,b: a*b, range(1,n+1))

"""
    To save the trouble of writing trivial anonymous functions like lambda a,b: a*b, the operator module provides
    function equivalents for dozen of arithmetic operators.
"""
from operator import mul

def fact2(n):
    return reduce(mul, range(1, n+1))

"""
    The functools module brings a handful of higher order functions. The best known of them is probably reduce and map, filter.
    of other remaining funtions in functools, the most useful is partial and its variation, partial method.

    functools.partial is higher-order function that allows the partial application of a function. Given a function, a
    partial application produces a new callable with some of the arguments of the original function fixed.
    This is useful to adapt a function that takes one or more arguments to an API that requires a callback with fewer
    arguments.
"""
from functools import partial
triple = partial(mul, 3)
print(triple(7))
print(list(map(triple, range(1, 10))))

"""
    A more useful example involves the unicode.normalize function. If you work with text from many languages,
    you may want to apply unicode.normalize('NFC', s) to any string s before comparing or storing it. If you do
    that often, it's handy to have an nfc function to do so.
"""

import unicodedata, functools

nfc = functools.partial(unicodedata.normalize, 'NFC')
s1 = 'cafe'
s2 = 'cafe\u0301'
# print(s1, s2)
print(s1 == s2)
print(nfc(s1) == nfc(s2))
