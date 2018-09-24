# coding: utf-8

from multiprocessing.managers import BaseManager, NamespaceProxy
from multiprocessing import Queue
import inspect

class TestClass(object):
    def __init__(self, a):
        self.a = a
        self.q = Queue()

    def b(self):
        print(self.a)

    def q(self):
        print(self.q)

class AnotherClass(object):
    def __init__(self, a):
        self.a = a
        self.q = Queue()

    def c(self):
        print(self.a)

    def q(self):
        print(self.q)

class MyManager(BaseManager): pass

class ProxyBase(NamespaceProxy):
    _exposed_ = ('__getattribute__', '__setattr__', '__delattr__')

class TestProxy(ProxyBase): pass
class AnotherProxy(ProxyBase): pass


def register_proxy(name, cls, proxy):
    for attr in dir(cls):

        print("   register")
        print(attr)
        if inspect.ismethod(getattr(cls, attr)) and not attr.startswith("__"):
            proxy._exposed_ += (attr,)
            setattr(proxy, attr, 
                    lambda s: object.__getattribute__(s, '_callmethod')(attr))
    MyManager.register(name, cls, proxy)

register_proxy('test', TestClass, TestProxy)
register_proxy('another', AnotherClass, AnotherProxy)

if __name__ == '__main__':
    manager = MyManager()
    manager.start()
    mt = manager.test(2)
    ma = manager.another(3)
    mt.b()
    ma.c()
    mt.a = 5
    ma.a = 6
    mt.b()
    ma.c()
    qa = ma.q()
    qb = mb.q()