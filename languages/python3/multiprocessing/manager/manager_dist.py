# coding: utf-8

from multiprocessing import Process, Manager


class TheBall(object):
    def __init__(self):
        self.q={}


def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()
    d['tb'].q["hahaha"] = "hohooh"
    print(d)
    print(l)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))
        d["tb"] = TheBall()
        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)