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
GRID.setWallsRandom(int(GRID.gridWidth*GRID.gridHeight*GRID_WALL_RATIO))

running=True
runAStar = True
while running:

	## ----- QUIT MECHANISM -----
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False

	## ----- GAME MECHANISM -----
	GRID.draw()
	if runAStar:
		result = GRID.runAStarAlgorithm()
		if result in [0,1]:
			d = {0:'No solutions', 1:'End reached'}
			print(d[result])
			runAStar = False

	## ----- PYGAME -----
	pygame.display.update()
	screen.fill( (0,0,0) ) #reset surface
	clock.tick(fps)

pygame.quit()
exit()