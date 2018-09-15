import sched
import time
from threading import Thread, Lock

#
# class SomeClass(Thread):
#
#     def __init__(self):
#
#
#     def do_something(sc):
#         print "Doing stuff..."
#         # do your stuff
#         # s.enter(60, 1, do_something, (sc,))
#         #
#         #

class MyThread(Thread):
    def __init__(self):
        ''' Constructor. '''
        self.lock = Lock()
        self.isruning = False
        Thread.__init__(self)
        self.s = sched.scheduler(time.time, time.sleep)

    def stop(self):
        with self.lock:
            for event in self.s.queue:
                self.s.cancel(event)

    def run(self):
        self.task()

    def next(self):
        self.s.enter(5, 1, self.task, ())
        self.run()


    def task(self):
        with self.lock:
            if self.isruning:
                return
            else:
                self.isruning = True

        print("Send event")
        self.stop()

        with self.lock:
            self.isruning = False
        self.next()




if __name__ == '__main__':
    mt = MyThread()
    mt.start()
    print('on running')

    time.sleep(12)
    print('stop')

#     sm.start()
#
#     sm.task()
#     sm.task()
#
#     sm.task()
#
#
# callss
# s = sched.scheduler(time.time, time.sleep)
