"""
    Below is a decorator that clocks every invocation of the decorated function and prints the elapsed time,
    the arguments passed, and the result of the call.
"""
import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result= func(*args)
        elapsed = time.perf_counter()-t0
        name = func.__name__
        arg_str = ",".join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r'%(elapsed, name, arg_str, result))
        return result
    return clocked

@clock
def factorial(n):
    return 1 if n<2 else n*factorial(n-1)

@clock
def snooze(seconds):
    time.sleep(seconds)

print('*'*40, 'Calling snooze(.123)')
snooze(.123)
print('*'*40, 'Calling factorial(6)')
print('6! = ', factorial(6))