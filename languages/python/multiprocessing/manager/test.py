# coding: utf-8
import multiprocessing
from multiprocessing.managers import BaseManager, NamespaceProxy
from multiprocessing import Queue, Process
import time
import sys

class Worker(Process):
    def __init__(self, name, shared, mode, to=None, *args):
        super(Worker, self).__init__() 
        self.name = name      # Unique name (Ex: t1, t2, t3, ...)
        self.mode = mode      # 'productor' or 'consomator'
        self.to = to          # productor message destination
        self.shared = shared  # Contain all shared Queue()

    def run(self):
        time.sleep(3)
        print(" - name : "+self.name+", shared : "+str(self.shared))
        if self.mode == "productor":
            print("   productor")
            while True:
                print(" = "+self.name+": self.shared.list_queue : "+str(self.shared.list_queue))
                time.sleep(2)
                self.shared.get_q(self.to).put("Custom message from "+self.name)
        else:
            print("   consomator")
            while True:
                print(" = "+self.name+": self.shared.list_queue : "+str(self.shared.list_queue))
                message = self.shared.get_q(self.name).get()
                print(message)

class Master():
    """shared object wetween process"""
    def __init__(self):
        self.list_queue = {}
        self.list_process = {}
        self.mana = multiprocessing.Manager()
        self.mana.start()
    
    def create_worker(self, name, mode, to=None):
        self.list_queue[name]   = self.mana.Queue()
        self.list_process[name] = Worker(name, self, mode, to)  # Init  process
        self.list_process[name].start()                         # Start process

    def get_q(self, name):
        return self.list_queue[name]

# class MyManager(BaseManager): pass

# MyManager.register('Master', Master)


if __name__ == "__main__":
    BaseManager.register('Master', Master)
    mana = BaseManager()
    mana.start()
    master = mana.Master()
    master.create_worker("t2","productor","t1")  # Send data to t1
    #master.create_worker("t3","productor","t1")  # Send data to t1
    master.create_worker("t1","consomator")      # Receive data

    # signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C')

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    print(signal, frame)
    sys.exit(0)
