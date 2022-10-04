import pygame.font

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (255,230,230)
        self.font = pygame.font.SysFont(None, 35)

        # Prepare the initial score image.
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendred image."""
        score_str = "High Score: " + str(self.stats.p2_score) + "    Current Score: " + str(self.stats.p1_score)
        self.p1_score_image = self.font.render(score_str, True, self.text_color,
                                                self.ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self.p1_score_rect = self.p1_score_image.get_rect()
        self.p1_score_rect.center = self.screen_rect.center

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.p1_score_image, self.p1_score_rect)
