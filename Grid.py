import pygame
import random
from Node import *

class Grid():
    def __init__(self,screen,pixelSize):
        self.screen=screen
        self.pixelSize = pixelSize
        w,h = pygame.display.get_surface().get_size()
        self.gridWidth, self.gridHeight = w//pixelSize, h//pixelSize
        self.grid=[[Node(j,i,self.pixelSize) for j in range(self.gridWidth)] for i in range(self.gridHeight)]
        self.gridCopy=None
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
        self.saveGrid()

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
        elif len(self.openSet)>=300:
            return 2
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

    def reset(self):
        self.grid=[[Node(j,i,self.pixelSize) for j in range(self.gridWidth)] for i in range(self.gridHeight)]
        start_node=self.grid[self.start[1]][self.start[0]]
        start_node.calculateF(self.end[0], self.end[1])
        start_node.state = 'start'
        self.openSet = [start_node]
        self.grid[len(self.grid)-1][len(self.grid[0])-1].state='end'

    def saveGrid(self):
        self.gridCopy=[[Node(j,i,self.pixelSize) for j in range(self.gridWidth)] for i in range(self.gridHeight)]
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                self.gridCopy[row][col].state=self.grid[row][col].state
                self.gridCopy[row][col].f=self.grid[row][col].f

    def loadGrid(self):
        self.grid=[[Node(j,i,self.pixelSize) for j in range(self.gridWidth)] for i in range(self.gridHeight)]
        for row in range(len(self.gridCopy)):
            for col in range(len(self.gridCopy[0])):
                self.grid[row][col].state=self.gridCopy[row][col].state
                self.grid[row][col].f=self.gridCopy[row][col].f
        
    def resetAlgo(self):
        self.loadGrid()  ##  Load gridCopy
        start_node=self.grid[self.start[1]][self.start[0]]
        start_node.calculateF(self.end[0], self.end[1])
        start_node.state = 'start'
        self.openSet = [start_node]
        self.grid[len(self.grid)-1][len(self.grid[0])-1].state='end'