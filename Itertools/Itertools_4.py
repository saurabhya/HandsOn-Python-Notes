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