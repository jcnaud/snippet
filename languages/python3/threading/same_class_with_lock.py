#!/usr/bin/env python
# coding: utf-8

import threading
import time

class Controller(threading.Thread):
    def __init__(self,p1):
        self.p1 = p1

        self.lock = threading.Lock()

    def run(self):
        print('run')

        t1 = threading.Thread(target=self.new_thread)
        t1.start()

        # First process
        while True:
            time.sleep(1)
            with self.lock:
                self.p1 = 'toto'
                time.sleep(0.1)
                print(self.unified_function('controller'))

    def new_thread(self):
        # Second process
        while True:
            time.sleep(1)
            with self.lock:
                self.p1 = 'tata'
                time.sleep(0.5)
                print(self.unified_function('new_thread'))

    def unified_function(self, user):
        return 'data from : '+self.p1+' and '+user


if __name__ == "__main__":
    p1 = 'toto'
    cont   = Controller(p1)
    cont.run()
