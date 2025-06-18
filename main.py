# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	pygame.init()
	print("Starting Asteroids!")
	print("Screen width:", SCREEN_WIDTH)
	print("Screen height:", SCREEN_HEIGHT)

	game_clock= pygame.time.Clock()
	dt = 0
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	Shot.containers = (shots, updatable, drawable)
	asteroidfield = AsteroidField()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT /2))
	while pygame.get_init():
		dt = game_clock.tick(60) / 1000
		updatable.update(dt)
		
		screen.fill("black")
		

		for asteroid in asteroids:
			
			if  asteroid.collision_check(player):
				print("Game over!")
				sys.exit()
		
		for entity in drawable:
			entity.draw(screen)

		pygame.display.flip()

		for event in pygame.event.get():
   			 if event.type == pygame.QUIT:
       				 return

if __name__ == "__main__":
    main()
