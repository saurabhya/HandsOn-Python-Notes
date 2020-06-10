"""
    In multiprocessing, process are spawned by creating a Process object and then calling its start() method.
    process follows the API of threading.Thread. A trivial example of a multiprocess program is:
"""
from multiprocessing import Process

def f(name):
    print('Hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

