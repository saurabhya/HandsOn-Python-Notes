"""
    Multiprocessing supports two types of communication channel between processes.

    The Queue class is near clone of the queue.Queue.
"""

from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q, ))
    p.start()
    print(q.get())
    p.join()

# Queues are thread and process safe