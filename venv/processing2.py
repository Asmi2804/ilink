import multiprocessing
from multiprocessing import *

def cube(n):
    return n * n * n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    #create a object for pool 
    pool = multiprocessing.Pool(processes=3)
    # map function
    results = pool.map(cube, numbers)

    pool.close()
    pool.join()

    print(results)
