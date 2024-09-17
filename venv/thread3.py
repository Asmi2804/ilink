import threading
from threading import *
import time

mylock=threading.Lock()

def task(mylock,msg):
    mylock.acquire()
    for i in range(5):
        print(msg)
    time.sleep(2)
    mylock.release()

t1=threading.Thread(target=task,args=(mylock,"Hello"))
t2=threading.Thread(target=task,args=(mylock,"Welcome"))
t1.start()
t2.start()
        
