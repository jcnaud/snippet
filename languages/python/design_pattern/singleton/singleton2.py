# coding: utf-8

# Singleton/ClassVariableSingleton.py
class SingleTone(object):
    __instance = None
    q = []
    def __new__(cls):
        if SingleTone.__instance is None:
            SingleTone.__instance = object.__new__(cls)
        #SingleTone.__instance.val = val
        return SingleTone.__instance
    def create_queue(self, val):
        SingleTone.q.append(val)


class Manager(object):
    def __init__(self):
        self.singletone = SingleTone()
 

if __name__ == "__main__":
    m1 = Manager()
    m2 = Manager()
    m3 = Manager()
    m1.singletone.create_queue("toto_1")
    m2.singletone.create_queue("toto_2")
    m3.singletone.create_queue("toto_3")
    print(m1.singletone.q)
