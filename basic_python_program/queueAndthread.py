﻿import Queue
from threading import Timer, Thread, Event
import time

class test_thread(Thread):
    def __init__(self, q):
        Thread.__init__(self)
        self.q = q
        self.stop_event = Event()
    def run(self):
        q = self.q
        while not self.stop_event.isSet():
            try:
                a, b, c = q.get(block=True, timeout=1)
            except Queue.Empty:
                print "empty queue"
                continue
            print a, b, c
            q.task_done()
        print "thread end"
    def join(self, timeout=None):
        print "thread join"
        self.stop_event.set()
        Thread.join(self, timeout)

q = Queue.Queue(10)

consumer_thread = test_thread(q)
consumer_thread.start()

for i in range(100):
    q.put([i, i+1, i+2])
q.join()
consumer_thread.join()
print "done"

