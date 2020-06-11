"""
    Depending on the platform, multiprocessing supports three ways to start a process.
    These start methods are:
    * spawn
    * fork
    * forkserver

    On Unix using the spawn or forkserver start methods will also start a resource tracker
    process which tracks the unlinked named system resources (such as named semaphores or
    SharedMemory objects) created by processes of the program.


    To select a start method you use the set_start_method() in the
    if __name__ == '__main__' clause of the main module. For example
"""

import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target= foo, args=(q,))
    p.start()
    print(q.get())
    p.join()