# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 01:16:24 2019

@author: Antiochian
"""
#INPUT ALGORITHM TO TEST HERE:#
import quicksort
###############################

import random
import bubblesort
import time

def sorttest(N,M):
    attempts = 100
    print("Testing...")
    timelist = []
    for k in range(attempts):
        n = random.randint(2,N)
        array = []
        for i in range(n):
            array.append(random.randint(0,M))
        correct = bubblesort.bubblesort(array)
        t0 = time.time()
        #INPUT ALGORITHM TO TEST HERE:#
        testanswer = quicksort.quicksort(array)
        ###############################
        timelist.append(time.time()-t0)
        if testanswer != correct:
            print("Error detected!")
            print("Input Array = ",array)
            print("Answer: ",testanswer)
            print("Desired: ",correct)
            return
    print("OK! - ",attempts," trials completed.")
    mean_time = sum(timelist)/len(timelist)
    print('Average time: ', round(mean_time,8)," seconds")
    return 

if __name__ == '__main__':
    N = int(input("N: "))
    M = int(input("M: "))
    sorttest(N,M)