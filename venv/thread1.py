import threading
from threading import *

def square_value(array,result):
    for i in array:
        print(i)
        result.append(i*2)

def cube_value(array,result):
    for i in array:
        print(i)
        result.append(i*3)

if __name__ == "__main__":
    list1=[1,2,3,4,5]
    square=[]
    cube=[]
    # create a object for Thread
    t1=threading.Thread(target=square_value, args=(list1,square))
    t2=threading.Thread(target=cube_value,args=(list1,cube))
    # start the thread object
    t1.start()
    t2.start()
    # wait till the thread function execute
    t1.join()
    t2.join()
    print(square)
    print(cube)
