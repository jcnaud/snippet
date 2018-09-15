# coding: utf-8

# Test two way communication

import multiprocessing


import time

def foo(conn):
    conn.send([42, None, 'hello'])
    print(conn.recv())
    conn.close()

if __name__ == '__main__':

    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=foo, args=(child_conn,))
    p.start()
    time.sleep(1)
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    time.sleep(1)
    parent_conn.send('toto')
    p.join()