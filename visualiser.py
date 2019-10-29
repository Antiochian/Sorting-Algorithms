# -*- coding: utf-8 -*- python3
"""

Sorting Visualiser
Created on Sun Oct 27 14:45:40 2019

@author: Antiochian
"""
import pygame
import random
import numpy as np
from bubblesort import *
from quicksort import *

#optional flags
colorfade = True #makes the brightness of each bar proportional to its value
uniformdist = True #makes the final result evenly-spaced bars
algorithm = "quick" #also accepts "bubble"

#color settings
white = (255,255,255)
red = (220, 50, 47) #m1 = red
blue = (38, 139, 210) #m2 = blue
green = (133,153,0)
darkblue = (7,54,66)
beige = (253,246,227)

bgcolor = darkblue
barcolor = green


#parameters
Nx,Ny = (800,480)
barwidthscale = 0.9
defaultN = 200 #number of bars
defaultM = 500 #maximum possible number of element in array

animFPS = 10000
menuFPS = 60

#pygame setup
pygame.init()
window = pygame.display.set_mode( (Nx,Ny) )
window.fill(bgcolor)
pygame.display.update()
pygame.display.set_caption("Sorting Visualiser")
surf = pygame.Surface( (Nx,Ny))
window.blit(surf,(0,0))
clock = pygame.time.Clock() 

######### ALGORITHMS ############
def bubblesort_recorder(array):
    while True:
        unsorted = True
        for i in range(1,len(array)):
            if array[i-1] > array[i]:
                array[i-1],array[i] = array[i],array[i-1]
                global record
                record = np.append(record,[array],axis = 0)
                unsorted = False
        if unsorted:
            return array
def quicksort_recorder(A):
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
            global record
            if any(A != record[-1,:]):
                record = np.append(record,[A],axis = 0)
    A[b-1],A[start] = A[start],A[b-1]
    if any(A != record[-1,:]):
        record = np.append(record,[A],axis = 0)
    return b-1
##################################################
    
def drawframe(row):
    #set up scale
    scale = Ny/max(row)
    barwidth = Nx/len(row)
    index = 0
    window.fill(bgcolor)
    #DEBUG: Draw only 1st bar:
    for i in range(len(row)):
        if colorfade:
            currentbarcolor = (0,0,0)
            currentbarcolor = (barcolor[0] * row[i]/max(row), barcolor[1] * row[i]/max(row), barcolor[2] * row[i]/max(row))
        else:
            currentbarcolor = barcolor
        barheight = row[i]*scale
        pygame.draw.rect(surf, currentbarcolor, (i*barwidth, Ny-barheight, barwidth*barwidthscale, barheight))
        index += 1
    return
    
def play_animation(record):
    for i in range(record.shape[0]): #for each row
        surf.fill(bgcolor)
        drawframe(record[i,:]) 
        clock.tick(animFPS)
        window.blit(surf,(0,0))
        pygame.display.update()
        
        for event in pygame.event.get(): #detect events
            if event.type == pygame.QUIT or pygame.key.get_pressed()[27]: #detect attempted exit
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[114]:
                menusetup()
                return
    return
        
def menusetup(N = defaultN, M = defaultM):
    #generate array
    array = []
    if uniformdist:
        for i in range(N):
            array.append(i+1)
        np.random.shuffle(array)
    else:
        for i in range(N):
            array.append(random.randint(0,M))
    global record
    record = np.array([array])
    if algorithm == "quick":
        quicksort_recorder(array)
    elif algorithm == "bubble":
        bubblesort_recorder(array)
    surf.fill(bgcolor)
    drawframe(record[0,:])
    window.blit(surf,(0,0))
    pygame.display.update()
    return


menusetup()
while True:
    clock.tick(menuFPS)
    for event in pygame.event.get(): #detect events
        if event.type == pygame.QUIT or pygame.key.get_pressed()[27]: #detect attempted exit
            pygame.quit()
            sys.exit() 
        if event.type == pygame.VIDEORESIZE: #detect resize
            (Nx, Ny) = event.size
            window = pygame.display.set_mode((Nx, Ny), pygame.RESIZABLE)
            surf = pygame.display.set_mode((Nx, Ny), pygame.RESIZABLE)
        if pygame.mouse.get_pressed()[0] or pygame.key.get_pressed()[32]:
            play_animation(record)  
        if pygame.key.get_pressed()[114]:
            menusetup()
            


        
        
        
        
        
        
        
        
        
        
        
        
        
