import pygame
from pygame.locals import *
#window characteristics - pixels
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

#game area characteristics
AREA_WIDTH = 300
AREA_HEIGHT = 600


#game constants in "brick units"
WIDTH = 10
HEIGHT = 20

assert AREA_HEIGHT/HEIGHT == AREA_WIDTH/WIDTH, "Sizing issues, check ratios bruh"

EDGE = AREA_HEIGHT/HEIGHT

assert not EDGE%10

#shape catalog
NONE = []
O = ["XX XX"]
T = ["OXO XXX","XO XX XO","XXX OXO","OX XX OX"]
L = ["XO XO XX","XXX XOO","XX OX OX","OOX XXX"]
J = ["OX OX XX","X00 XXX","XX XO XO","XXX OOX"]
S = ["OXX XXO","XO XX OX"]
Z = ["XXO OXX","OX XX XO"]
I = ["X X X X","XXXX"]
#SHAPES
SHAPES = [O,L,J,S,Z,T,I]
#SHAPE_COLORS = {O:,T:,L:,J:,S:,Z:}

#Physics
FREEFALL = 10
SIDESHIFT =10

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0, 0, 255)
RED = (255,0,0)
GREEN = (0,255,0)
SOMETHING = (255,255,0)
ELSE = (0,255,255)
ALSO = (255,0,255)
FINALLY = (128, 128, 0)
BRICK_COLORS = [RED, GREEN, SOMETHING, ELSE, ALSO, FINALLY]

#animation stuff
FPS = 30
fpsClock = pygame.time.Clock()

#input enums
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"
NOTHING = "NONE"
INPUT = [UP, DOWN, LEFT, RIGHT, NONE]

