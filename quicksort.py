# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 17:56:44 2019

@author: Antiochian 
"""
def quicksort(A):
    start = 0
    end = len(A)-1
    quicksort_recursive(A,start,end)
    return A

def quicksort_recursive(A,start,end):
    if start < end:
        p_index = partition(A,start,end)
        
        quicksort_recursive(A,start,p_index-1)
        quicksort_recursive(A,p_index+1,end)
    else:
        return A
    
    
def partition(A,start,end):   
    p = end
    pivot = A[p]
    A[start], A[p] = A[p],A[start]
    b = start+1 #index of border
    for i in range(start+1,end+1):
        if A[i] < pivot:
            #put behind border
            A[b],A[i] = A[i],A[b]
            b += 1 
    A[b-1],A[start] = A[start],A[b-1]
    return b-1
       
if __name__ == '__main__':
    #some example list to sort
    A = [13,41,5,212,54,6,29,3,17]
    print(A)
    print(quicksort(A))