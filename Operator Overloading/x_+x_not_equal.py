"""
    Everybody expects that x == +x, and that is true almost all the time in Python,
    but there are two cases in the standard library where x != +x.

    The first case involves the decimal.Decimal class. You can have x != +x
    if x is a Decimal instance created in an arithmetic context and +x if thn
    evaluated in a context with different settings. For example, x is calculated
    in a context with a certain precision, but the precision, but the precision
    of the context is changed and then +x is evaluated.
"""

import decimal
ctx = decimal.getcontext()
ctx.prec = 40
one_third = decimal.Decimal('1')/ decimal.Decimal('3')
print(one_third)
print(one_third == +one_third)
ctx.prec = 28
print(one_third == +one_third)
print(+one_third)

"""
    The fact is that each occurence of the expression +one_third produces a new decimal
    instance from the value of one_third, but using the precision of the current arithmetic context.
"""

"""
    Second case where x != +x you can find in the collections.Counter documentation.
    The counter class implements several arithmetic operators, including infix + to add
    the tallies from two counter instances. However, for practical reasons, Counter addition discards
    from the result any item with a negative or zero count. And the prefix + is a shortcut for adding
    an empty Counter, therefore it produces a new Counter preserving only
    tallies that are gretaer than zero.
"""
from collections import Counter

ct = Counter('abracadabra')
print(ct)
ct['r'] = -3
ct['d'] = 0
print(ct)
print(+ct)