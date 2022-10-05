import pygame
class PauseScreen():
	def __init__(self, screen):
		"""Initialize the Background."""
		self.screen = screen

		#Load the pause screen 
		self.image = pygame.image.load('images/pause_screen.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Load the pause scree at the center
		self.rect.centerx = self.screen_rect.centerx

	def blitme(self):
		"""Draw the background."""
		self.screen.blit(self.image, self.rect)
