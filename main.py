#!/usr/bin/env python
#This file exists to mess around and look at how pygame does things. That's it.
import pygame, sys
from pygame.locals import *
from constants import * 
import random
rects = []
pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('TESTIN')

WHITE = (255,255,255)
BLACK = (0,0,0)
shapeX = WINDOW_WIDTH/2
shapeY = WINDOW_HEIGHT/2
orie = 0

    
def redoRect():
    global shapeX, shapeY, rects, orie
    DISPLAYSURF.fill(WHITE)
    rects = []
    shapeX = WINDOW_WIDTH/2
    shapeY = WINDOW_HEIGHT/2
    orie+=1
    orie%=4
    for line in T_SHAPE[orie].split(" "):
        for box in line:
            if box=="X":
                rects.append(pygame.Rect(shapeX,shapeY,EDGE,EDGE))
                #pygame.draw.rect(DISPLAYSURF, BLACK, muhRect)
            shapeX+=EDGE
        shapeX = WINDOW_WIDTH/2
        shapeY+=EDGE
                
    
redoRect()
while True:
    
    


                
    for square in rects:
        pygame.draw.rect(DISPLAYSURF, BLACK, square)
    
    #pygame.draw.rect(DISPLAYSURF, BLACK, muhRect)

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                redoRect()
            
    
    pygame.display.update()
    
    fpsClock.tick(FPS)