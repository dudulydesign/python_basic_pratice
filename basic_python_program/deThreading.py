#python [numpy]=[matlab]?

import threading #導入threading 模組
from multiprocessing import Queue #使用多核心模組 Queue

#define first thread
#num is a 參數 to job1, q is Queue object, and lock is a lock of threading

def job1(num, q, lock):
    lock.acquire() #lock this threading, do not work before finish self work
    sum = 0
    for i in range(num):
        sum += i

        q.put(sum) #put a anwer to Queue, get after
        lock.release() #unlock this threading, and start others threading
        #The function in thread do not alow with return, else its going to be worng

#define second thread
def job2(num, q, lock):
    lock.acquire()
    sum = 0
    for i in range(num):
        sum += i**10

    q.put(sum)
    lock.release()

#define main program
def main():
    lock = threading.Lock() #name a lock object
    q = Queue() #open a Queue object
    t1 = threading.Thread(target=job1, args=(8,q,lock))
                                #name a thread obj as "t1"
                                #the obj is going to call "job1"
                                #import q and lock to "t1" for control

    t2 = threading.Thread(target=job2, args=(8,q,lock))

    t1.start() #start thread "t1"
    t2.start() #start thread "t2"
    t1.join() #before finish thread "t1" stop program
    t2.join() #before finish thread "t2" stop program

    #check Queue is empty or not, we use "q.get()" if not empty
    while not q.empty():
        print(q.get())

print "END Section!"
print "=" * 100

if __name__== '__main__' : main()

