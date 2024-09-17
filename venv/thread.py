import threading
from threading import *
import time

# print the thread name
print(threading.current_thread().name)
# current is alive or not
print(threading.current_thread().is_alive())
# set the thread name by ourself
def worker():
    print(f"Thread {threading.current_thread().name} is starting")

def display():
    for i in range(1,6):
        print("Hi")
        time.sleep(1)

def print_numbers():
    for i in range(1,11):
        print(i)
        time.sleep(1)   

t1=threading.Thread(target=display)
t2=threading.Thread(target=print_numbers)
t3=threading.Thread(target=worker ,name="Thread1")
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Done!")