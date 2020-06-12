"""
    A manger object returned by Manager() controls a server process which holds
    Pyhton objects and allows other processes to manipulate then using proxies.

    A manager returned by Manager() will support types list, dict, Namespace, Lock,
    etc.
"""

from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()
        print(d)
        print(l)

"""
    Server process managers are more flexible than using shared memory objects because they can be made
    to support arbitrary object types. Also, a single manager can be shared by processes on different computers
    over a network. They are, however, slower than using shared  memory.
"""