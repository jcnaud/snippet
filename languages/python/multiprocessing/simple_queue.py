
# coding: utf-8
import multiprocessing

import time

def foo(q):
    q.put('hello')


if __name__ == '__main__':
    multiprocessing.set_start_method('forkserver')
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=foo, args=(q,))
    p.start()
    time.sleep(2)
    print(q.get())
    p.join()