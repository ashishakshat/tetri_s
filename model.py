from constants import *
import library
import string
import random

def snapToEdge(coord):
    """return closest multiple of EDGE"""
    if(coord%EDGE>EDGE/2):
        return EDGE*(coord/EDGE+1)
    else:
        return EDGE*(coord/EDGE)

class wall(object):
    """The actual wall of pieces that have fallen into place.
    Instance attributes:
        _bricks: All the bricks down there. It's a list. Bricks
        take care of their own position.
    This is pretty much it."""
    
    def __init__(self):
        self._bricks = []
    
    
    def draw(self, view):
        for brick in self._bricks:
            brick.draw(view)
            
    def getBricks(self):
        """Return a copy of the list of bricks"""
        return self._bricks[:]
        
    def addBrick(self, brick):
       # print brick._y-1
        #assert not (brick._y-1)%EDGE
        #brick._y = snapToEdge(brick._y)+1
        #print brick._y -1
        self._bricks.append(brick)
        
    def performSweep(self):
        newWall = []
        rowCount = [0 for i in range(HEIGHT)]
        for brick in self._bricks:
       #     print rowCount
        #    print brick._y/EDGE
            #print brick._y
            rowCount[brick._y/EDGE]+=1
        #print rowCount
        for brick in self._bricks:
            if(rowCount[brick._y/EDGE]!=WIDTH):
                newWall.append(brick)
                
        self._bricks = newWall
        
        cumulative = [0 for i in range(HEIGHT)]
        
        for x in range(HEIGHT-1, -1, -1):
            if(x==HEIGHT-1):
                cumulative[x] = 1 if rowCount[x]==10 else 0    
            else:
                cumulative[x] = cumulative[x+1]
                if(rowCount[x]==10):
                    cumulative[x]+=1
        
        for brick in self._bricks:
            brick._y += EDGE*cumulative[brick._y/EDGE]
           
        
        
class brick(object):
    """A brick. This is what exists in that wall up there"""
    
    def __init__(self, x, y):
        """x and y are in the 'grid coordinate system', not
        in pixels. We treat the screen as a grid of bricks."""
        #some color picker thing
        self._color = BRICK_COLORS[random.randint(0,len(BRICK_COLORS)-1)]
        self._x = x
        self._y = y
        
    def draw(self, view):
        library.drawSquare(self._x, self._y, self._color, view)
        
class shape(object):
    """One of the falling shapes"""
    def __init__(self, shape):
        assert shape in SHAPES
        self._shape = shape
        self._breadth = 0
        self._tall = 0
        self._orientations = len(shape)
        self._orientation = 0
        self._bricks = []
        self._x = WIDTH/2
        self._y = -2 * EDGE
        self._arrangeBricks()
        #populate bricks:
        
    def _arrangeBricks(self):
        self._bricks = []
        rows = self._shape[self._orientation].split()
        self._breadth = len(rows[0])
        self._tall = len(rows)*EDGE
        x = self._x
        y = self._y
        for row in rows:
            for letter in row:
                if letter == "X":
                    self._bricks.append(brick(x,y))
                x+=1
                
            x = self._x
            y = y + EDGE
        
        if(self._x + self._breadth > WIDTH):
            self.left()
        #return self._checkBottomed()
        
        #return bottom
    def fall(self):
        self._y += 1
        #self._fallen = self._arrangeBricks()
        self._arrangeBricks()
           
    def draw(self, view):
        for brick in self._bricks:
            brick.draw(view)
            
   # def fallen(self):
    #    return self._fallen
    
    def rotate_right(self):
        self._orientation+=1
        if(self._orientation==self._orientations):
            self._orientation = 0
        
        self._arrangeBricks()
        
    def rotate_left(self):
        self._orientation-=1
        if(self._orientation==-1):
            self._orientation = len(self._shape)-1
        
        self._arrangeBricks()
        
        
    def left(self):
        if(self._x>0):
            self._x -= 1
            self._arrangeBricks()
    
    def right(self):
        if(self._x<WIDTH-self._breadth):
            self._x += 1
            self._arrangeBricks()


class Game:
    def __init__(self):
        self._wall = wall()
        self._currentShape = NONE
        self._rotated = False
        self._goLeft = SIDESHIFT
        self._goRight = SIDESHIFT
        
    def gameStep(self, view, key):
       # print type(self._currentShape)
        if(self._currentShape == NONE):
            self._wall.performSweep()
            self._currentShape = shape(SHAPES[random.randint(0,len(SHAPES)-1)])
        else:
            self._currentShape.fall()
            if(key==UP):
                if not self._rotated:
                    self._currentShape.rotate_right()
                    if(self._colliding()):
                        self._currentShape.rotate_left()
                    self._rotated = True
            if(key==LEFT):
                if self._leftClear():
                    self._currentShape.left()
            if(key==RIGHT):
                if self._rightClear():
                    self._currentShape.right()
            if(key==DOWN):
                for i in range(FREEFALL):
                    if(not self._checkBottomed()):
                        self._currentShape.fall()
                    
            if(key==NOTHING):
                self._rotated = False
            if(self._checkBottomed()):
                print self._currentShape._y
                self._stopShape()
        
        
        
        
        if(self._currentShape!=NONE):
            self._currentShape.draw(view)
        
        self._wall.draw(view)
        
    def _colliding(self):
        for wallBrick in self._wall.getBricks():
            for shapeBrick in self._currentShape._bricks:
                if wallBrick._y-EDGE <= shapeBrick._y < wallBrick._y+EDGE and shapeBrick._x == wallBrick._x:
                    return True
        
        return False
    
    def _stopShape(self):
        for brick in self._currentShape._bricks:
            self._wall.addBrick(brick)
        self._currentShape = NONE
    
    def _checkBottomed(self):
        if self._currentShape._y==WINDOW_HEIGHT-self._currentShape._tall:
            #print self._currentShape._y
            return True
        
        for wallBrick in self._wall.getBricks():
            for shapeBrick in self._currentShape._bricks:
                if shapeBrick._y+EDGE == wallBrick._y and shapeBrick._x == wallBrick._x:
              #      print self._currentShape._y
                    return True
                
        return False

    def _leftClear(self):
        for wallBrick in self._wall.getBricks():
            for shapeBrick in self._currentShape._bricks:
                if wallBrick._y - EDGE <= shapeBrick._y < wallBrick._y+EDGE and shapeBrick._x == wallBrick._x+1:
                    return False
    
        return True
    
    def _rightClear(self):
        for wallBrick in self._wall.getBricks():
            for shapeBrick in self._currentShape._bricks:
                if wallBrick._y - EDGE <= shapeBrick._y < wallBrick._y+EDGE and shapeBrick._x == wallBrick._x-1:
                    return False
    
        return True
    
    


def initGame():
    return Game()
    


