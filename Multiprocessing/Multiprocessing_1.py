"""
    Multiprocessing is a package that supports processes using an API similar
    to the threading module. The multiprocessing package offers both local
    and remote concurrency, effectively side-stepping the Global Interpreter Lock
    by using subprocesses instead of threads. Due to this, the multiprocessing module
    allows the programmer to fully levarage mulitple processors on a given machine.
    It runs on both Unix and Windows.

    The multiprocessing module also introduces APIs which do not have analogs
    in the threading module. A prime example of this is the Pool Object which offers
    a convenient means of parallelizing the execution of a function across multiple
    input values, distributing the input data across processes(data parallelism).
    The following example demonstrates the common practice of defining such functions
    in a module so that child processes can successfully import that module.
    This basic example of data parallelism using Pool.
"""
from multiprocessing import Pool

def f(x):
    return x*x

if __name__=='__main__':
    with Pool(5) as p:
        print(p.map(f,[1,2,3]))