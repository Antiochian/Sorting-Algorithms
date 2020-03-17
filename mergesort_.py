# -*- coding: utf-8 -*- python3
"""
Created on Tue Mar 17 11:21:59 2020

@author: Antiochian
"""
import numpy as np

def recorder(array):
    global record
    record = np.array([array.copy()])
    merge_sort(array)
    return record


def merge_sort(arr):
    global record
    subl = split(arr,[])
    res = subl
    while len(res) > 1:
        record = np.append(record,[[item for sublist in res for item in sublist]],axis = 0)
        pivot = len(res)//2
        left = res[:pivot]
        right = res[pivot:]
        res = []
        while left != [] and right != []:
            res.append(merge(left.pop(),right.pop()))
        res += left+right
    record = np.append(record,[res[0]],axis = 0)
    return res[0]

def split(arr,sublists):
    if len(arr) == 1: #if arr is 1-item long
        sublists.append(arr)
        return sublists
    
    pivot = len(arr)//2
    split(arr[:pivot],sublists)
    split(arr[pivot:],sublists)
    return sublists   

def merge(A,B):
    global record
    C = []
    while A != [] and B != []:
        if A[-1] > B[-1]:
            C.append(A.pop())
        else:
            C.append(B.pop())
    while A != []:
        C.append(A.pop())
    while B != []:
        C.append(B.pop())
    C.reverse()
    return C