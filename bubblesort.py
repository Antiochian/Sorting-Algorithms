# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 01:08:32 2019

@author: Antiochian
"""

#bubble sort
#this is a slow algorithm  - O(n^2) - but its useful as a naive algorithm for stress testing

def bubblesort(array):
    while True:
        unsorted = True
        for i in range(1,len(array)):
            if array[i-1] > array[i]:
                array[i-1],array[i] = array[i],array[i-1]
                unsorted = False
        if unsorted:
            return array


if __name__ == '__main__':
    array = [int(x) for x in input().split()]
    print(bubblesort(array))