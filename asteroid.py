import pygame
from player import *
import random


class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, surface):
		pygame.draw.circle(surface, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += (self.velocity * dt)
	
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return

		else:
			random_angle = random.uniform(20, 50)
			spawn_vector1 = self.velocity.rotate(-random_angle)
			spawn_vector2 = self.velocity.rotate(random_angle) 
			spawn_radius = self.radius - ASTEROID_MIN_RADIUS
			asteroid_spawn1 = Asteroid(self.position.x, self.position.y, spawn_radius)
			asteroid_spawn2 = Asteroid(self.position.x, self.position.y, spawn_radius)
			asteroid_spawn1.velocity = spawn_vector1 * 1.2
			asteroid_spawn2.velocity = spawn_vector2 * 1.2
