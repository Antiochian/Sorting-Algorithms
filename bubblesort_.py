# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 01:08:32 2019

@author: Antiochian
"""

#bubble sort
#this is a slow algorithm  - O(n^2) - but its useful as a naive algorithm for stress testing
import numpy as np

def recorder(array=[4,1,22,13,5,6,2]):
    global record
    record = [array.copy()]
    while True:
        unsorted = True
        for i in range(1,len(array)):
            if array[i-1] > array[i]:
                array[i-1],array[i] = array[i],array[i-1]
                record = np.append(record,[array],axis = 0)
                unsorted = False
        if unsorted:
            return record #note that array is also sorted in-place