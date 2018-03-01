#!/usr/bin/env python
# coding: utf-8

import queue
import threading
from time import sleep

def worker(q,i):
    while True:
        item = q.get()
        if item is None:
            break
        print("Worker "+str(i)+" with item "+str(item))
        sleep(1)
        q.task_done()

def main(num_worker_threads):
    q = queue.Queue()
    threads = []
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker,args=(q,i))
        #t.setDaemon(True)
        t.start()
        threads.append(t)

    ## put in queue
    for item in range(10): 
        q.put(item)

    # block until all tasks are done
    q.join()

    # stop workers
    for i in range(num_worker_threads):
        q.put(None)
    for t in threads:
        t.join()


if __name__ == "__main__":
    main(2)




# from Queue import Queue
# from threading import Thread

# def do_stuff(q):
#   while True:
#     print q.get()
#     q.task_done()

# q = Queue(maxsize=0)
# num_threads = 10

# for i in range(num_threads):
#   worker = Thread(target=do_stuff, args=(q,))
#   worker.setDaemon(True)
#   worker.start()

# for x in range(100):
#   q.put(x)

# q.join()