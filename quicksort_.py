# -*- coding: utf-8 -*- python3
"""
Created on Fri Jan 10 03:45:37 2020

@author: Antiochian
"""
import numpy as np

def recorder(A):
    global record
    record = [A.copy()]
    start = 0
    end = len(A)-1
    quicksort_recursive(A,start,end)
    return record

def quicksort_recursive(A,start,end):
    if start < end:
        p_index = partition(A,start,end)
        
        quicksort_recursive(A,start,p_index-1)
        quicksort_recursive(A,p_index+1,end)
    else:
        return A

def partition(A,start,end):   
    global record
    p = end
    pivot = A[p]
    A[start], A[p] = A[p],A[start]
    b = start+1 #index of border
    for i in range(start+1,end+1):
        if A[i] < pivot:
            #put behind border
            A[b],A[i] = A[i],A[b]
            b += 1 
            for ela, elr in zip(A,record[-1]):
                if ela != elr:
                    record = np.append(record,[A],axis = 0)
    A[b-1],A[start] = A[start],A[b-1]
    if any(A != record[-1,:]):
        record = np.append(record,[A],axis = 0)
    return b-1