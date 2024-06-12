import pygame

class Node():
    def __init__(self,x,y,size):
        self.x=x
        self.y=y
        self.size=size
        self.state=None
        self.f = None

    def draw(self,screen):
        offset=2
        color = (255,255,255)
        if self.isWall():
            color = (125,125,125)
        elif self.isOpen():
            color=(0,255,0)
        elif self.isClose():
            color=(255,0,0)
        elif self.state in ['start','end']:
            color=(255,255,0)
        pygame.draw.rect(screen, color, pygame.Rect(self.x*self.size+offset, self.y*self.size+offset,
                                                            self.size-offset, self.size-offset))

    def calculateF(self, endX,endY):
        self.f = (self.x-endX)**2 + (self.y-endY)**2

    def setOpen(self):
        if self.state==None: self.state = 'open'

    def setClose(self):
        if self.state=='open': self.state = 'closed'

    def isOpen(self):
        return self.state=='open'
    
    def isClose(self):
        return self.state=='closed'
    
    def isWall(self):
        return self.state=='wall'
    
    def resetNode(self):
        self.state=None
        self.f = None
