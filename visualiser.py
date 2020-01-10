# -*- coding: utf-8 -*- python3
"""

Sorting Visualiser
Created on Sun Oct 27 14:45:40 2019

@author: Antiochian
"""
import pygame
import random
import sys
import numpy as np
import bubblesort_
import quicksort_
import heapsort_
"""
------------------
TABLE OF CONTENTS:
------------------
1. Parameters/Setup
2. Algorithm Library
3. Helper functions
4. Main Loop
Note: The actual sorting step is precomputed by the menusetup() function in the background
"""
#optional flags
colorfade = True #makes the brightness of each bar proportional to its value
uniformdist = True #makes the final result evenly-spaced bars
algorithm = "bubblesort" #default algorithm, also accepts "bubble"

#color settings
white = (255,255,255)
red = (220, 50, 47) #m1 = red
blue = (38, 139, 210) #m2 = blue
green = (133,153,0)
darkblue = (7,54,66)
beige = (253,246,227)
transparentgrey = (8,17,23,10)

#set up theme
textcolor = white
pausecolor = transparentgrey
bgcolor = darkblue
barcolor = green


#parameters
Nx,Ny = (800,480)
barwidthscale = 0.9
defaultN = 100 #number of bars
defaultM = 500 #maximum possible number of element in array

animFPS = 60
menuFPS = 30

#pygame setup
pygame.init()
window = pygame.display.set_mode( (Nx,Ny) )
window.fill(bgcolor)
pygame.display.update()
pygame.display.set_caption("Sorting Visualiser")
surf = pygame.Surface( (Nx,Ny))
surf.fill(bgcolor)
pausescreen = pygame.Surface( (Nx,Ny), pygame.SRCALPHA ) #pause screen
window.blit(surf,(0,0))
clock = pygame.time.Clock() 

######### ALGORITHMS ############
        
algorithm_dictionary = {}
algorithm_dictionary['bubblesort'] = bubblesort_.recorder
algorithm_dictionary['quicksort'] = quicksort_.recorder
algorithm_dictionary['heapsort'] = heapsort_.recorder

#################################
    
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
    variableanimFPS = animFPS #reset animFPS to default
    #variableanimFPS = min(120,int(len(record)/(5))) #normalised animation speed
    labelstring = algorithm+", n = "+str(defaultN)+", FPS = "+str(variableanimFPS)
    labelsurf = renderlabel(labelstring)
    for i in range(record.shape[0]): #for each row
        surf.fill(bgcolor)
        drawframe(record[i,:]) 
        clock.tick(variableanimFPS)
        window.blit(surf,(0,0))
        window.blit(labelsurf,(0,0))
        pygame.display.update()
        for event in pygame.event.get(): #detect events
            if event.type == pygame.QUIT or pygame.key.get_pressed()[27]: #detect attempted exit
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[114]:
                menusetup()
                return
            if pygame.key.get_pressed()[273]:
                variableanimFPS += 5
                labelstring = algorithm+", n = "+str(defaultN)+", FPS = "+str(variableanimFPS)
                labelsurf = renderlabel(labelstring)
            if pygame.key.get_pressed()[274]:
                variableanimFPS -= 5
                labelstring = algorithm+", n = "+str(defaultN)+", FPS = "+str(variableanimFPS)
                labelsurf = renderlabel(labelstring)
    return
        
def menusetup( displaymenu = True,N = defaultN, M = defaultM):    
    #generate array
    fadein(transparentgrey,500)
    surf.fill(bgcolor)
    array = []
    if uniformdist:
        for i in range(N):
            array.append(i+1)
        np.random.shuffle(array)
    else:
        for i in range(N):
            array.append(random.randint(0,M))
            
    global record
    record = algorithm_dictionary[algorithm](array)  
    
    drawframe(record[0,:])
    window.blit(surf,(0,0))
    if displaymenu:
        window.blit(pausescreen,(0,0))
        rendertext()
        menuimg = pygame.image.load('menu.png') 
        mx,my = 297,195
        window.blit(menuimg,(int((Nx-mx)/2),int(-100 + Ny - my)))
    pygame.display.update()
    return

def fadein(finalcolor,fadelength,startcolor = (0,0,0,0)): #fadelength is in milliseconds
    frames = int(fadelength*menuFPS/1000)
    #frametime = 1/FPS defunct variable for time.sleep(frametime) functionality
    #this is in case one wants to decouple the animation rate from the frame rate
    for framenumber in range(frames+1):
        colorfraction = framenumber/10
        Rcolorchange = -startcolor[0] + finalcolor[0]
        Gcolorchange = -startcolor[1] + finalcolor[1]
        Bcolorchange = -startcolor[2] + finalcolor[2]
        Acolorchange = -startcolor[3] + finalcolor[3]

        RED = max(int(startcolor[0] + colorfraction*Rcolorchange),0)
        GREEN = max(int(startcolor[1] + colorfraction*Gcolorchange),0)
        BLUE = max(int(startcolor[2] + colorfraction*Bcolorchange),0)
        ALPHA = max(int(startcolor[3] + colorfraction*Acolorchange),0)
        color = (RED,GREEN,BLUE,ALPHA)
        pausescreen.fill(color)
        window.blit(pausescreen, (0,0) )
        pygame.display.update()
    return       

def rendertext(topsize=50,bottomsize=20,spacer=40,myfont='dfkaisb',verticaloffset=100):
    #(spacer is the spacing between the title and subtitle)
    titlefont = pygame.font.SysFont(myfont,topsize)
    pausefont = pygame.font.SysFont(myfont, bottomsize)
    titletextsurf = titlefont.render("Sorting-Algorithms",True,textcolor)
    (titletextwidth, titletextheight) = (max(titletextsurf.get_width(),1),max(titletextsurf.get_height(),1))
    pausetextsurf = pausefont.render("Press 'R' to restart // Press 'Esc' to quit", True, textcolor)
    (pausetextwidth, pausetextheight) = (max(pausetextsurf.get_width(),1),max(pausetextsurf.get_height(),1))
    pausetextposition = int( (Nx-pausetextwidth)/2 ), int( (Ny-pausetextheight)/2 - verticaloffset) #20pix gap between textlines
    titletextposition = int( (Nx-titletextwidth)/2 ), int(pausetextposition[1] - 0.5*(spacer+pausetextheight+titletextheight))
    # BLIT TEXT AND UPDATE SCREEN #
    window.blit(pausetextsurf, pausetextposition)
    window.blit(titletextsurf, titletextposition)
    pygame.display.update()
    return

def renderlabel(labelstring="Testlabel"):
    labelfont = pygame.font.SysFont('dfkaisb', 20)
    labelsurf = labelfont.render(labelstring,True,textcolor)
    return labelsurf

menusetup()
#MAIN LOOP#
while True:
    clock.tick(menuFPS)
    for event in pygame.event.get(): #detect events
        if event.type == pygame.QUIT or pygame.key.get_pressed()[27]: #detect attempted exit
            pygame.quit()
            sys.exit() 
        elif event.type == pygame.VIDEORESIZE: #detect resize
            (Nx, Ny) = event.size
            window = pygame.display.set_mode((Nx, Ny), pygame.RESIZABLE)
            surf = pygame.display.set_mode((Nx, Ny), pygame.RESIZABLE)
            menusetup()
        if pygame.key.get_pressed()[114]: #reset key
            menusetup()
        if pygame.mouse.get_pressed()[0] or pygame.key.get_pressed()[32]: #default play
            play_animation(record)
        if pygame.key.get_pressed()[49]: #1
            algorithm = "quicksort"
            menusetup(False)
            play_animation(record)
        elif pygame.key.get_pressed()[50]: #2
            algorithm = "bubblesort"
            menusetup(False)
            play_animation(record)
        elif pygame.key.get_pressed()[51]: #3
            algorithm = "heapsort"
            menusetup(False)
            play_animation(record)
