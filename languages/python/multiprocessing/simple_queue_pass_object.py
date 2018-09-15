
# coding: utf-8
import multiprocessing

import time

class Toto:
    def __init__(self, message):
        self.message = message
        self.table = ["toto"]


def foo(q):
    t = Toto("Je suis ici")

    print(t)
    print(t.table)
    print(id(t.table))
    q.put(t)


if __name__ == '__main__':
    multiprocessing.set_start_method('forkserver')
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=foo, args=(q,))
    p.start()
    time.sleep(2)
    res = q.get()
    print(res)
    print(res.message)
    print(res.table)
    print(id(res.table))

    p.join()