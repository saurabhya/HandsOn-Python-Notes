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

"""
    There's an easy way to generate this sequence with the itertools.cycle() function.
    This function takes an iterable inputs as an argument and returns an infinte iteratot
    over the values in inputs that returns an infinte iterator over the values in inputs
    that returns to the beginning once the end of inputs is reached. So, to produce the
    alternating sequence of 1s and -1s, you could do this:
"""
alternating_ones = it.cycle([1, -1])

"""
    The goal of this part is to produce a single function that can generate any first order
    recurrence relation - just pass it P, Q, and an initial value. One way to do this is with
    itertools.accumulate().

    The accumulate() function takes two arguments - an iterable inputs and a binary function func()
    - and returns an iterator over accumulated results of applying func to elements of inputs.
    It is rouughly equivalent to the following generator:
"""
def accumulate(inputs, func):
    itr = iter(inputs)
    prev = next(itr)
    for cur in itr:
        yield prev
        prev = func(prev, cur)

# For example
import operator
print(list(it.accumulate([1,2,3,4,5], operator.add)))

"""
    The second argument of accumulate() defaults to operator.add(),
    so the previous example can be simplified to:
    list(it.accumulate([1,2,3,4,5]))
    [1,3,6,10,15]


    Pasing the built-in min() to accumulate() will keep track of a running minimum
"""
print(list(it.accumulate([9,21,17,5,11,12,2,6], min)))

"""
    More complex function scan be passed to accumulate() with lambda expressions
"""
print(list(it.accumulate([1,2,3,4,5], lambda x, y: (x+y)/2)))

"""
    THe order of the arguments in the binary function passed to accumulate() is important.
    The first argument is always the previously accumulated result and the argument is always
    the next element of the input iterable. For example, consider the diference in output of
    the following expressions:
"""

print(list(it.accumulate([1,2,3,4,5], lambda x, y: x-y)))

print(list(it.accumulate([1,2,3,4,5], lambda x, y: y-x)))