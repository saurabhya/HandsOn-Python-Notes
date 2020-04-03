"""
    Our previous implementation of make_average was not efficient. We stored all the values in the historical series
    and computed thier sum every time averager was called. A better implentation would just store the total and the
    number of items so far, and compute the mean fom these two numbers.

    Now we will see a broken implementation, just to make the point.
"""
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total/count
    return averager

avg = make_averager()
print(avg(10)) # local variable 'count' referenced before assignment

"""
    the problem is that the statement count += 1 actually means the same as count = count +1, when count is a number or any immutable type.
    So we are actually assigning to count in the body of averager, and that makes it a local variable. the same problem
    affects the total variable.

    we did not have this problem before in closure.py because we never assigned to the series name; we only called series.append and
    invoked sum and len on it. So we took advantage of the fact that lists are mutable.

    But with immutable types like numbers, strings, tuple, etc. all you can do is read, but never update. If you try to rebind them
    as in count = count +1, then you are implictely creating a local variable count. it is no longer a free variable, and therefore
    it is not saved in the closure.

    To work around this, the non l;ocal declaration was introduced in Python 3. It lets you flag a variabl;e as a free variable even
    when it is assigned a new value within the function. if a new value is assigned to a nonlocal variable,
    the binding stored in the closure is changed. A correct implementation of our newest make_averager is defined in NonLocal-declarationex.py
"""
