# coding: utf-8

import multiprocessing
import signal
import sys
import logging

import time
from service import *


class Controller(object):
    def __init__(self, q_parent=None):
        #self.children =  ['Opc']
        self.children =  ['Opc','Cli','Job','Api']

        # Create minimal Queue
        self.q = {}
        self.p = {}
        self.q["parent"] = q_parent
        self.q["self"] = multiprocessing.Queue()

    def start_one(self, child):
        """Start one child"""
        logging.info("Start child : "+str(child))
        self.q[child] = multiprocessing.Queue()
        print(globals()[child])
        self.p[child] = globals()[child](self.q["self"],self.q[child])
        # self.p[child] = multiprocessing.Process(
        #     target=globals()[child], 
        #     args=(self.q["self"],self.q[child]))
        self.p[child].start()

    def start_all(self):
        """Start all children"""
        logging.info("Start all children")
        for child in self.children:
            self.start_one(child)

    def stop_one(self, child):
        """Stop one child"""
        logging.info("Stop child : "+str(child))
        #TODO

    def stop_all(self):
        """Stop all children"""
        logging.info("Stop all children")
        for child in self.children:
            self.stop_one(child)

    def kill_one(self, child):
        """Kill one child"""
        logging.info("Kill child : "+str(child))
        #TODO

    def kill_all(self):
        """Kill all children"""
        logging.info("Kill all children")
        for child in self.children:
            self.kill_one(child)

    def test_one(self, child):
        """Test one child"""
        logging.info("Test child : "+str(child))
        #TODO
        return 0
    
    def test_all(self):
        """Test all children"""
        for child in self.children:
            res = self.test_one(child)
        # TODO
        return 0

    def run(self):
        """Start children"""
        self.start_all()

        print("ici")
        
        self.q['Opc'].put({ "type":"cmd","lol":"toto"})
        self.q['Opc'].put({ "type":"req","lol":"toto"})


        print("la")
        print(self.q['self'].get())
        print(self.q['self'].get())

        print("la")

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
    # Logs
    logging.basicConfig(level=logging.INFO)
    mpl = multiprocessing.log_to_stderr()
    mpl.setLevel(logging.INFO)

    # Run
    contr = Controller()
    contr.run()
