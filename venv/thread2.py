import concurrent.futures
from concurrent.futures import *
import time,random

def study(fname,lname):
    for i in range(5):
        print(f"{fname} {lname} is studying {i}")
        time.sleep(random.random())

def listening(fname,lname):
    for i in range(5):
        print(f"{fname} {lname} is listening music {i}")
        time.sleep(random.random())

if __name__ =="__main__":
    
    argument=[["John","Robert"],["Smith","Roy"]]
    # ThreadPoolExecutor function
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(study,"John","Smith")
        executor.submit(listening, "Robert", "Roy")
        # map function
        executor.map(study,*argument)