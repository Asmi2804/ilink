import multiprocessing
from multiprocessing import *

def square_value(array):
    result=[]
    for i in array:
        print(i)
        result.append(i*2)
    print(result)    

if __name__=="__main__":
    list1=[1,2,3,4,5]
    square=[]
    # create object for multiprocessing
    p1=multiprocessing.Process(target=square_value, args=([1,2,3,4,5],))
    # the object to start
    p1.start()
    # wait till the execution stop
    p1.join()
    #print(squar