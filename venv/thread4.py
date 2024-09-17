import threading
from threading import *
from time import sleep
lock=threading.Lock()
class Bus:
    def __init__(self, name, available_seats,l):
        self.available_seats=available_seats
        self.name=name
        self.l=l
    def reserve(self,need_seats):
        self.l.acquire()
        print("Available seats are:", self.available_seats)
        if self.available_seats>=need_seats:
            nm=current_thread().name
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats-=need_seats
        else:
            print("Sorry! seats are not available.")
        self.l.release()    

b1=Bus("ABC travels", 2,lock)
t1=Thread(target=b1.reserve, args=(2,), name="Jay")
t2=Thread(target=b1.reserve, args=(1,), name="Raj")
t1.start()
t2.start()