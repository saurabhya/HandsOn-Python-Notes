"""
    set_start_method() should not be used more than once in the program.

    Alternatively, you can use get_context() to obtain a context object.
    Context objects have the same API as the multiprocessing module, and allow
    one to use multiple start methods in the same program.
"""

import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target= foo, args=(q,))
    p.start()
    print(q.get())
    p.join()