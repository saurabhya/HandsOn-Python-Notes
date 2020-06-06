"""
    A recurrence relation is a way of describing a sequence of numbers with a recursive formula.
    One of the best-known recurrence relations is the one that describes the Fibonacci sequence.
    It is common to see fibonacci seqeunce prduced with a generator:
"""
import itertools as it

def fibs():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

"""
    The recurrence ralation descibing the fibonacci numbers is called a second order recurrence
    relation because, to calculate the next number in the sequence, you need to look back two
    numbers behind it.
"""

"""
    we've already seen how count() can generate the sequence of non-negative integers, the even integers,
    and the odd integers. You can also use it to generate the sequence 3n = 0 3, 6, 9... and 4n.
"""

count_by_three = it.count(step=3)
count_by_four = it.count(step= 4)

"""
    In fact, count() can produce sequences of multiple of any number you wish. These sequences can be
    describedwith first-order recurrence relations.

    Another easy example of a first-order recurrence relation is the constant sequence n, n, n, n..., where
    n is any value you'd like. Itertools provides an easy way to implement this sequence as well, with the
    repeat() function.
"""

all_ones = it.repeat(1)
all_twos = it.repeat(2)

"""
    If you need a finite sequence of repeated values, you can set a stopping point by passing a positive
    integer as a second argument.
"""
five_ones = it.repeat(1, 5)
five_twos = it.repeat(4, 3)