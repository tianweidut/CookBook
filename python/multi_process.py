#coding: utf-8

from multiprocessing import Process, Queue, Pipe
from multiprocessing import Lock


def f(q):
    q.put([44, 44, 44])


def f2(conn):
    print 'in f2 child process'
    conn.send([44, 42])
    conn.close()


def f3(i, lock):
    lock.acquire()
    print "in f3 %s %s" % (i, lock)
    lock.release()


def test_queue():
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print q.get()
    p.join()


def test_pipe():
    parent_conn, child_conn = Pipe()
    p = Process(target=f2, args=(child_conn,))
    p.start()
    print parent_conn.recv()
    p.join()


def test_sync():
    lock = Lock()

    for i in range(10):
        p = Process(target=f3, args=(i, lock,))
        p.start()


if __name__ == "__main__":
    #test_pipe()
    test_sync()
