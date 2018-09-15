# coding: utf-8

import multiprocessing
import signal
import sys

import time
from cli import cli
from job import job

class Controller(object):
    def __init__(self, q_parent=None):
        self.children = ['cli','job']
        # self.children = ['opc','cli','job','api']

        # Create Queues and process
        self.q = {}
        self.p = {}
        self.q["parent"] = q_parent
        self.q["self"] = multiprocessing.Queue()

        for child in self.children:
            self.q[child] = multiprocessing.Queue()
            self.p[child] = multiprocessing.Process(
                target=globals()[child], 
                args=(self.q["self"],self.q[child]))

    def run(self):
        """Start children"""
        for child in self.children:
            self.p[child].start()
        

        self.q['cli'].put({ "lol":"toto"})
        self.q['cli'].put({ "lol":"toto"})
        self.q['cli'].put({ "lol":"toto"})
        self.q['cli'].put({ "lol":"toto"})
        self.q['cli'].put({ "lol":"toto"})
        self.q['cli'].put({ "lol":"toto"})
        self.q['job'].put({ "lol":"toto"})

        print(self.q['self'].get())
        print(self.q['self'].get())


        signal.signal(signal.SIGINT, signal_handler)
        print('Press Ctrl+C')
        signal.pause()

        for child in self.children:
            self.p[child].join()

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    print(signal, frame)
    sys.exit(0)

if __name__ == '__main__':
    contr = Controller()
    contr.run()
