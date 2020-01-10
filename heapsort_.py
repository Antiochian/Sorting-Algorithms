# -*- coding: utf-8 -*- python3
"""
Created on Fri Jan 10 04:02:44 2020

@author: Antiochian
"""

import numpy as np

def recorder(array):
    global record
    record = [array.copy()]
    n = len(array)
    #make max heap
    for i in range(len(array),-1,-1):
        #iterate backwards from len -> 0 until heap is done
        heapify(array,n,i)
    #extract sorted list from max heap
    for root in range(len(array)-1,0,-1): 
        array[root],array[0] = array[0],array[root]
        heapify(array,root,0)
        if any(record[-1] != array):
            record = np.append(record,[array],axis = 0)
    return record
    
def heapify(array,n,i): #i = root index
    #indexex
    current_largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    #check if left > parent
    if left < n and array[left] > array[current_largest]:
            current_largest = left
    if right < n and array[right] > array[current_largest]:
            current_largest = right
        
    #update values if current_largest has changed
    if current_largest != i:
        array[current_largest], array[i] = array[i], array[current_largest]
        global record #add to record
        record = np.append(record,[array],axis = 0)
        heapify(array,n,current_largest) #only persist if i has changed
