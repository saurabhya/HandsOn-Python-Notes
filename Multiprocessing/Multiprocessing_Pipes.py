"""
    The Pipe() function returns a pair of connection objects connected by a pipe
    which by default is duplex (two-way).
"""

from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn, ))
    p.start()
    print(parent_conn.recv())
    p.join()

"""
    The two connection objects returned by Pipe() represent the two ends of the pipe.
    Each connection object has send() and recv() methods (among others). Note that data
    in a pipe may become corrupted if two processes (or threads) try yo read from or write
    to the same end of the pipe at the same time. Of course there is no risk of corruption
    from processes using different ends of the pipe at the same time.
"""
