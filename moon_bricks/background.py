import pygame

class Forground():

    def __init__(self, screen):
        """Initialize the foreground"""
        self.screen = screen

        # Load the ball image and set its rect.
        self.image = pygame.image.load('images\p1_wins.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set the location at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw Foreground at its current location."""
        self.screen.blit(self.image, self.rect)
