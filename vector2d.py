#Create Vector 2d plane class
import sys

class vector2d:
    def __init__(self, x=-1 , y=-1, angle=0):
        self.x = x
        self.y = y
        self.angle = angle
    
    def coordinate(self,x,y):
        self.x = x
        self.y = y
    
    def getCoordinate(self):
        return (self.x,self.y)
        