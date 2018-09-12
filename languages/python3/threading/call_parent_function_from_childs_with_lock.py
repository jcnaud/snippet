#!/usr/bin/env python
# coding: utf-8

import threading
import time

class Parent(object):
    def new_thread(self):
        return Child(parent=self)
    def make_echo(self, thread, data):
        return data

class Child(threading.Thread):

    def __init__(self, parent=None):
        self.parent = parent
        super(Child, self).__init__()

    def run(self): # exectued  when thread.start()
        with lock:
            print("Processing ..")
            time.sleep(1)
            print(self.parent.make_echo(self, 42))


if __name__ == "__main__":

    p    = Parent()
    lock = threading.Lock()

    for i in range(5):
        thread = p.new_thread()
        thread.start()