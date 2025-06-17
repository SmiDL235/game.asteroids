# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *


def main():
	pygame.init()
	print("Starting Asteroids!")
	print("Screen width:", SCREEN_WIDTH)
	print("Screen height:", SCREEN_HEIGHT)

	game_clock= pygame.time.Clock()
	dt = 0

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT /2))
	while pygame.get_init():
		screen.fill("black")
		player.draw(screen)
		
		pygame.display.flip()
		dt = game_clock.tick(60) / 1000 
		for event in pygame.event.get():
   			 if event.type == pygame.QUIT:
       				 return
	
if __name__ == "__main__":
    main()
