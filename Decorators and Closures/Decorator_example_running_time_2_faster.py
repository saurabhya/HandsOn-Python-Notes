"""
    Memorization with functools.lru_cache

    A very practical decorator is functolls.lru_cache. It implements memorization: an optimization technique that
    works by saving the results of previous invocations of an expensive functions, avoiding repeat computations
    on previously used arguments. The letters lru stands for least recently used, meaning that the growth of the
    cache is limited by discarding the entries that have been read for a while.
    In Decorator_example_running_time_2.py
        The waste is obvious: fibonacci(1) is called eight times, fibonacci(2) five times, etc, But if just add
        two lines to use lru_cache, performance is much improved.
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

@functools.lru_cache()
@clock
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2)+fibonacci(n-1)

print(fibonacci(6))

"""
    Besides making silly recursive algorithms viable, lru_cache really shines in applications that need to fetch
    information from the web.
    It's important to note that lru_cache can be tuned by passing two optional arguments.Its full signature is:

    fuctools.lru_cache(maxsize=128, typed=False)

    The maxsize argument determines how many call results are stored. After the cache is full, older results are discarded
    to make room. For optional performance, axsize should be a power of 2. The typed argument, if set to True, stores results
    of different argument types separartely, i.e. distinguishing between float and integer arguments that are normally considered
    equal, like 1 and 1.0. By the way, because lru_cache uses a dict to store the results, and the keys are made from the
    positional and keyword arguments used in the calls, all the arguments taken by the decorated function must be hashable.
"""