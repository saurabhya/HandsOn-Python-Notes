"""
    The clock decorator we used earlier has a few shortcomings: it does not support keyword arguments, and it masks the
    __name__ and __doc__ of the decorated function.
    Following implementation uses the functools.wraps decorator to copy the relevant attributes from func to clocked.
    Also, in this new version, keyword arguments are correctly handled.
"""

import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(args) for arg in args))
        if kwargs:
            pairs = ['%s=%r'%(k,w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', ',join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r'%(elapsed, name, arg_str, result))
        return result
    return clocked

@clock
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2)+fibonacci(n-1)

print(fibonacci(6))