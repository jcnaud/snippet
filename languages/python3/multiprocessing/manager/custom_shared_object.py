# coding: utf-8

import multiprocessing
from multiprocessing.managers import BaseManager

class MyManager(BaseManager): pass

def Manager():
    m = MyManager()
    m.start()
    return m 

class Counter(object):
  def __init__(self):
    self._value = 0

  def update(self, value):
    self._value += value

  def get_value(self):
      return self._value

MyManager.register('Counter', Counter)

def update(counter_proxy, thread_id):
  counter_proxy.update(1)
  print(counter_proxy.get_value(), 't%s' % thread_id, \
    multiprocessing.current_process().name)
  return counter_proxy

def main():
  manager = Manager()
  counter = manager.Counter()
  pool = multiprocessing.Pool(multiprocessing.cpu_count())
  for i in range(10):
    pool.apply(func=update, args=(counter, i))
  pool.close()
  pool.join()

  print('Should be 10 but is %s.' % counter.get_value())

if __name__ == '__main__':
  main()