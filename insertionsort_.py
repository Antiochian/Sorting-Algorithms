# -*- coding: utf-8 -*- python3
"""
Created on Fri Jan 10 11:54:53 2020

@author: Antiochian
"""
import numpy as np

def recorder(array):
    global record
    record = [array.copy()]
    changed = True
    while changed == True:
        changed = False
        for i in range(len(array)-1):
            if array[i+1] < array[i]:
                changed = True
                array[i+1],array[i] = array[i],array[i+1]
                record = np.append(record,[array],axis = 0)

    return record
    

#    return record

