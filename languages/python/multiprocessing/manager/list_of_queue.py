# coding: utf-8
import multiprocessing
from multiprocessing.managers import BaseManager, NamespaceProxy
from multiprocessing import Queue, Process, Manager
import time
import sys
import signal

class Worker(Process):
    def __init__(self, name, queues, confs, mode, to=None, *args):
        super(Worker, self).__init__() 
        self.name = name      # Unique name (Ex: t1, t2, t3, ...)
        self.mode = mode      # 'productor' or 'consomator'
        self.to = to          # productor message destination
        self.queues = queues  # Contain all queues Queue()
        self.conf = {}
        self.conf['all'] = confs  # Contain all queues Queue()
        self.process = None

    def run(self):
        time.sleep(3) # 
        if self.mode == "productor":
            print("   productor")
            while True:
                #print(" = "+self.name+": self.queues.list_queue : "+str(self.queues))
                time.sleep(1)
                self.queues[self.to].put("Custom message from "+self.name)
        elif self.mode == "consomator":
            print("   consomator")
            while True:
                #print(" = "+self.name+": self.queues.list_queue : "+str(self.queues))
                message = self.queues[self.name].get()
                print(message)
        else: # creator
            print("   creator")
            while True:
                time.sleep(1)
                print(self.process)


class Master():
    """queues object between process"""
    def __init__(self, ):
        self.mm = multiprocessing.Manager() # Manage Queue creation
        #self.mm = mana
        # self.my = MyManager()
        # self.my.start()
        #self.mana.start()
        self.process = {}
    
    def create_worker(self, name, queues, confs, mode, to=None):
        queues[name] = self.mm.Queue()

        self.process[name] = Worker(name, queues, confs, mode, to) # Init  process
        self.process[name].start()                                          # Start process
        #process[name] = self.process[name]

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    print(signal, frame)
    sys.exit(0)


if __name__ == "__main__":
    with Manager() as mana: # First manager to create list
        queues = mana.dict()
        confs = mana.dict()
        master = Master()
        master.create_worker("t2", queues, confs, "productor", "t1")  # Send data to t1
        master.create_worker("t3", queues, confs, "productor", "t1")  # Send data to t1
        master.create_worker("t1", queues, confs, "consomator")       # Receive data
        master.create_worker("t4", queues, confs, "creator")          # Receive data

        signal.signal(signal.SIGINT, signal_handler)
        print('Press Ctrl+C')

        # for process in master.list_process:
        #     process.join()
        signal.pause()

