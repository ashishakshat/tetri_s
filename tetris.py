#!/usr/bin/env python

import pygame, sys
from pygame.locals import *
from constants import * 
import random
import library
import model

view = library.initDraw()
game = model.initGame()
key = NOTHING

while True:
    
    
    #key = NOTHING
    #game.gameStep(view)
    #key = NOTHING if key in [LEFT,RIGHT] else key
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            key = event.key
        elif event.type == KEYUP:
            key = NOTHING
    
    if key == K_UP:
        key = UP
    elif key == K_DOWN:
        key = DOWN
    elif key == K_RIGHT:
        key = RIGHT
    elif key == K_LEFT:
        key = LEFT
    elif key == K_ESCAPE:
        pygame.quit()
        sys.exit()
    
    game.gameStep(view,key)
    
    library.step(view) #this draws too!