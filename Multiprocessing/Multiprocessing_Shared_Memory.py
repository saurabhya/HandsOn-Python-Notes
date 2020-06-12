"""
    When doing concurrent programming it is usually best to avoid using shared state as far as possible.
    This is particularly true when using multiple processes.

    However, if you really do need to use some shared data then multiprocessing provides a couple of ways
    of doing so.

    Shared Memory
        Data can be stored ina shred memory map using Value or Array.

"""

from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])

"""
    The 'd' and 'i' arguments used when creating num and arr are typecodes of the kind used by the array module:
    'd' indicates a double precision float and 'i' indicates a signed integer.
    These shared objects will be process and thread-safe.
"""