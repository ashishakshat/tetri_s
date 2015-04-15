"""library.py
This file interfaces with the pygame library. Anything that has to
be drawn gets sent here. Pygame takes care of the drawing."""

import pygame
from constants import *
import random
def drawSquare(x,y,color,view):
    """draw a square given its grid coordinates and color"""
    toDraw = pygame.Rect(x*EDGE,y,EDGE,EDGE)
    #color = BRICK_COLORS[random.randint(0,len(BRICK_COLORS)-1)]
    
    pygame.draw.rect(view, BLACK, toDraw)
    pass

def initDraw():
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), 0, 32)
    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption('bbbbbb')
    return DISPLAYSURF

def step(view):
    pygame.display.update()
    fpsClock.tick(FPS)
    view.fill(WHITE)
    pygame.draw.rect(view, BLUE, pygame.Rect(EDGE*WIDTH, 0, WINDOW_WIDTH-EDGE*WIDTH, EDGE*HEIGHT))