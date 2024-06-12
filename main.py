## ----- CENTER WINDOW -----
import os
os.environ["SDL_VIDEO_CENTERED"] = "1" # Centers game window

import pygame
from Grid import *

## ----- PYGAME VARIABLES -----
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('''A* Algorithm Visualiser''')
clock=pygame.time.Clock()
fps=120  ## Changes speed of visualiser

## ----- FONT -----
# pygame.font.init()
# font = pygame.font.SysFont('Bauhaus 93', 20)

## ----- GAME VARIABLES -----
GRID_PIXEL_SIZE = 10
GRID_WALL_RATIO = 1/3

## ----- GAME INIT -----
GRID = Grid(screen, GRID_PIXEL_SIZE)
n = int(GRID.gridWidth*GRID.gridHeight*GRID_WALL_RATIO)
GRID.setWallsRandom(n)

running=True
runAStar = True
loopAStar = True
print(f'Press: \n1. to turn the auto-restart on/off.\n2. to reset the grid and re-randomise wall placement.\n3. Replay current grid')
'''
Press:
1. to turn the auto-restart on/off.
2. to reset the grid and re-randomise wall placement.
3. Replay current grid
'''
while running:

	## ----- QUIT MECHANISM -----
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		## ----- BUTTON MECHANISM -----
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:  ##  Turn on and off looping algorithm
				loopAStar = not loopAStar
				if loopAStar: runAStar=True
				print(f'(1) Loop {"on" if loopAStar else "off"}')
			elif event.key == pygame.K_2:  ##  Reset grid
				GRID.reset()
				GRID.setWallsRandom(n)
				runAStar = True
				print(f'(2) Grid reset')
			elif event.key == pygame.K_3:  ##  Replay last
				GRID.resetAlgo()
				runAStar = True
				print(f'(3) A* reset')

	## ----- VISUALISER MECHANISM -----
	GRID.draw()
	if runAStar:
		result = GRID.runAStarAlgorithm()
		if result in [0,1,2]:
			d = {0:'No solutions', 1:'End reached',2:'Too slow'}
			print(d[result])
			##  Loop A* algorithm for satisfaction! :)
			if loopAStar:
				##  Reset and randomize
				GRID.reset()
				GRID.setWallsRandom(n)
			else:
				runAStar = False
	
	## ----- PYGAME -----
	pygame.display.update()
	screen.fill( (0,0,0) ) #reset surface
	clock.tick(fps)

pygame.quit()
exit()