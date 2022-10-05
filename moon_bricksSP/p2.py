import pygame

class P2():

    def __init__(self, screen, ai_settings):
        """Initialize the p2 and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the p2 image and set its rect.
        self.image = pygame.image.load('images/splayer.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start p2 at the LEFT center of the screen.
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for the plater's center.
        self.center = float(self.rect.centery)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

        # Hitter flags
        self.up_hitter = True
        self.down_hitter = False

    def update(self):
        """Update players position based on the movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.center -= self.ai_settings.player_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.player_speed_factor

        # Update the rect from self.center.
        self.rect.centery = self.center

    def blitme(self):
        """Draw p1 at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_p2(self):
        """Center p2 on the Screen"""
        self.rect.centery = self.screen_rect.centery
        self.center = self.screen_rect.centery
