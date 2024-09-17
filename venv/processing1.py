import multiprocessing
from multiprocessing import *

def square_value(array,result):
    for index,i in enumerate(array):
        result[index]=i*2  
    

if __name__=="__main__":
    list1=[1,2,3,4,5]
    # share data between the process
    square=multiprocessing.Array('i',5)
    p1=multiprocessing.Process(target=square_value, args=(list1,square))
    p1.start()
    p1.join()
    print(square[:])