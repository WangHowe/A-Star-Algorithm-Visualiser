import pygame
import random

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

class Grid():
    def __init__(self,screen,pixelSize):
        self.screen=screen
        self.pixelSize = pixelSize
        w,h = pygame.display.get_surface().get_size()
        self.gridWidth, self.gridHeight = w//pixelSize, h//pixelSize
        self.grid=[[Node(j,i,self.pixelSize) for j in range(self.gridWidth)] for i in range(self.gridHeight)]
        self.start = (0,0)
        self.end = (len(self.grid[0])-1, len(self.grid)-1)
        start_node=self.grid[self.start[1]][self.start[0]]
        start_node.calculateF(self.end[0], self.end[1])
        start_node.state = 'start'
        self.openSet = [start_node]
        self.grid[len(self.grid)-1][len(self.grid[0])-1].state='end'
        # self.closedSet = []

    def draw(self):
        for i in range(self.gridWidth):
            for j in range(self.gridHeight):
                self.grid[j][i].draw(self.screen)

    def setWall(self, row:int, column:int):
        '''Row and Column start from 0'''
        self.grid[column][row].state = 'wall'

    def setWallsRandom(self, n):
        for i in range(n):
            x,y=random.randint(0,self.gridWidth-1), random.randint(0,self.gridHeight-1)
            if (x,y )not in [(0,0), (self.gridWidth-1,self.gridHeight-1)]:
                self.setWall(x,y)

    def insertIntoOpenset(self, node:Node, insertTop=None):
        if self.openSet==[]:
            self.openSet.append(node)
        if insertTop==None: insertTop=len(self.openSet)
        for i in range(min(insertTop,len(self.openSet))):
            if node.f < self.openSet[i].f:
                self.openSet.insert(i, node)
                return
        self.openSet.insert(min(insertTop+1,len(self.openSet)), node)

    def runAStarAlgorithm(self):
        if self.openSet == []:
            return 0
        else:
            ## Find winner (smallest f)
            winnerI = 0
            winner = self.openSet[winnerI]

            ##  If winner is the end, stop
            if winner.x==self.end[0] and winner.y==self.end[1]:
                winner.state='end'
                return 1
            
            ##  Pop winner from openSet and move it to closedSet
            self.openSet.pop(winnerI)
            winner.setClose()
            # self.closedSet.append(winner)
                
            ##  Append neighbours to openSet
            neighbours = [(0,1), (0,-1), (1,0), (-1,0)]
            for xi,yi in neighbours:
                if winner.x+xi>=0 and winner.x+xi<=self.gridWidth-1 and winner.y+yi>=0 and winner.y+yi<=self.gridHeight-1:
                    if not self.grid[winner.y+yi][winner.x+xi].isClose() and not self.grid[winner.y+yi][winner.x+xi].isWall():
                        neighbour:Node = self.grid[winner.y+yi][winner.x+xi]
                        neighbour.calculateF(self.end[0],self.end[1])
                        neighbour.setOpen()
                        self.insertIntoOpenset( neighbour )
