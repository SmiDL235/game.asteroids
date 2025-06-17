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
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT /2))
	while pygame.get_init():
		dt = game_clock.tick(60) / 1000 
		updatable.update(dt)
		screen.fill("black")
		for player in drawable:
			player.draw(screen)
		
		pygame.display.flip()
		 
		for event in pygame.event.get():
   			 if event.type == pygame.QUIT:
       				 return
	
if __name__ == "__main__":
    main()
