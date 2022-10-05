import pygame
import random

class Ball():

    def __init__(self, screen, ai_settings, p1, p2, stats, sb, fg):
        """Initialize the ball and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.p1 = p1
        self.p2 = p2
        self.stats = stats
        self.sb = sb
        self.fg = fg

        # Load the ball image and set its rect.
        self.image = pygame.image.load('images\moon_ball.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start the ball at the CENTER of the screen.
        self.rect.center = self.screen_rect.center

        # Set the balls directions randomly
        self.dirs = ["downright", "downleft", "upright", "upleft"]
        self.up_left_dirs = ["upleft", "updleft"]
        self.down_left_dirs = ["downleft", "downdleft"]
        self.up_right_dirs = ["upright", "updright"]
        self.down_right_dirs = ["downright", "downdright"]
        self.dir_leftright_factor = 1
        self.dir_updown_factor = 0.5
        self.dir_leftright_factors = [0.5, 0.7, 1.1, 1.3, 1.7]
        self.dir_updown_factors = [0.4, 0.6, 0.8, 1, 1.7]
        self.dir = random.choice(self.dirs)

        # Set the float value for the the top and left
        self.left = float(self.rect.left)
        self.top = float(self.rect.top)

    def update(self):
        # Get random modifires.
        self.dir_updown_factor = random.choice(self.dir_updown_factors)
        self.dir_leftright_factor = random.choice(self.dir_leftright_factors)
        
        # Update the left,top based on the direction, i.e 'dir'.
        if self.dir == "downright":
            self.left += self.ai_settings.ball_speed_factor 
            self.top  += self.ai_settings.ball_speed_factor + self.dir_updown_factor

        if self.dir == "downleft":
            self.left -= self.ai_settings.ball_speed_factor + self.dir_leftright_factor
            self.top  += self.ai_settings.ball_speed_factor + self.dir_updown_factor

        if self.dir == "upright":
            self.left += self.ai_settings.ball_speed_factor + self.dir_leftright_factor
            self.top  -= self.ai_settings.ball_speed_factor

        if self.dir == "upleft":
            self.left -= self.ai_settings.ball_speed_factor + self.dir_leftright_factor
            self.top  -= self.ai_settings.ball_speed_factor + self.dir_updown_factor

        if self.dir == "updleft":
            self.left -= self.ai_settings.ball_speed_factor + self.dir_leftright_factor
            self.top  -= self.ai_settings.ball_speed_factor + self.dir_updown_factor

        if self.dir == "updright":
            self.left += self.ai_settings.ball_speed_factor + self.dir_leftright_factor
            self.top  -= self.ai_settings.ball_speed_factor + self.dir_updown_factor

        if self.dir == "downdright":
            self.left += self.ai_settings.ball_speed_factor + self.dir_leftright_factor
            self.top  += self.ai_settings.ball_speed_factor + self.dir_updown_factor

        if self.dir == "downdleft":
            self.left -= self.ai_settings.ball_speed_factor + self.dir_leftright_factor
            self.top  += self.ai_settings.ball_speed_factor + self.dir_updown_factor

        # Update the position based on left and top
        self.rect.top = self.top
        self.rect.left = self.left

        # Update the direction based on collisions.
        if self.rect.top <= 0:
            #Collision with upper edge
            if self.dir == 'upright' or self.dir == 'updright':
                self.dir = random.choice(self.down_right_dirs)
            if self.dir == 'upleft' or self.dir == 'updleft':
                self.dir = random.choice(self.down_left_dirs)

        if self.rect.bottom >= self.ai_settings.screen_height:
            #Collision with bottom edge
            if self.dir == 'downright' or self.dir == 'downdright':
                self.dir = random.choice(self.up_right_dirs)
            if self.dir == 'downleft' or self.dir == 'downdleft':
                self.dir = random.choice(self.up_left_dirs)

        # Update dir according to player collisions.
        if self.rect.colliderect(self.p1):
            #collision with player 1.
            if self.p1.down_hitter:
                self.dir = 'downleft'
            if self.p1.up_hitter:
                self.dir = 'upleft'
            # Increase ball speed
            self.ai_settings.ball_speed_factor += 0.005

        if self.rect.colliderect(self.p2):
            #collision with player 2.
            if self.p2.down_hitter:
                self.dir = 'downright'
            if self.p2.up_hitter:
                self.dir = 'upright'
            # Increase ball speed
            self.ai_settings.ball_speed_factor += 0.005

        # Make the game inactive on collision with edges.
        if self.rect.left <= 0:
            # Collision with the left edge
            # Make the mouse visible
            if self.dir == 'downleft' or self.dir == 'downdleft':
                self.dir = 'downdright'
            if self.dir == 'upleft' or self.dir == 'updleft':
                self.dir = 'updright'
            self.left += 10
            pygame.mouse.set_visible(True)
            self.stats.p1_score += 1
            self.ai_settings.reset_ball_speed()
            self.stats.game_active = False
            if self.stats.p1_score >= 11:
                self.fg.image = pygame.image.load('images\p1_wins.bmp')
                self.stats.game_end = True
                self.stats.p1_score = 0
                self.stats.p2_score = 0
                self.center_ball()
                self.p1.center_p1()
                self.p2.center_p2()
            self.sb.prep_score()

        if self.rect.right >= self.ai_settings.screen_width:
            # Collision with the right edge
            # Make the mouse visible
            if self.dir == 'downright' or self.dir == 'downdright':
                self.dir = 'downdleft'
            if self.dir == 'upright' or self.dir == 'updright':
                self.dir = 'updleft'
            self.left -= 10
            self.stats.p2_score += 1
            self.ai_settings.reset_ball_speed()
            pygame.mouse.set_visible(True)
            self.stats.game_active = False
            if self.stats.p2_score >= 11:
                self.fg.image = pygame.image.load('images\p2_wins.bmp')
                self.stats.game_end = True
                self.stats.p1_score = 0
                self.stats.p2_score = 0
                self.center_ball()
                self.p1.center_p1()
                self.p2.center_p2()
            self.sb.prep_score()
            
            
    def blitme(self):
        """Draw p1 at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ball(self):
        """Center the ball on the Screen"""
        self.rect.center = self.screen_rect.center
        self.top = (self.ai_settings.screen_height/2)
        self.left = (self.ai_settings.screen_width/2)
        self.dir = random.choice(self.dirs)
