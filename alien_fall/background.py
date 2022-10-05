import pygame
class Background():
	def __init__(self, screen):
		"""Initialize the Background."""
		self.screen = screen

		#Load the background 
		self.ground_image = pygame.image.load('images/bg_image.bmp')
		self.ground_rect = self.ground_image.get_rect()
		self.sun_image = pygame.image.load('images/bg_sun.bmp')
		self.sun_rect = self.sun_image.get_rect()
		self.screen_rect = screen.get_rect()

		#Load the ground at the bottom
		self.ground_rect.centerx = self.screen_rect.centerx
		self.ground_rect.bottom = self.screen_rect.bottom

		#Load the sun at the top
		self.sun_rect.centerx = self.screen_rect.centerx
		self.sun_rect.top = self.screen_rect.top

	def blitme(self):
		"""Draw the background."""
		self.screen.blit(self.ground_image, self.ground_rect)
		#self.screen.blit(self.sun_image, self.sun_rect)