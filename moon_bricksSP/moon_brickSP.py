import sys
import pygame
from settings import Settings
from p1 import P1
from p2 import P2
from ball import Ball
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from background import Forground

def run_game():
    #Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Bricks")
    
    # Make the stats and the scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make Player 1 & 2.
    p1 = P1(screen, ai_settings)
    p2 = P2(screen, ai_settings)

    # Make the ball and forground.
    fg = Forground(screen)
    ball = Ball(screen, ai_settings, p1, p2, stats, sb, fg)

    # Make the play button.
    play_button = Button(ai_settings, screen, "play")

    # Start the main loop for the game.
    while True:
        
        gf.check_events(p1, p2, stats, play_button, ball, screen)
        if stats.game_active:
            p1.update()
            p2.update()
            ball.update()
        gf.update_screen(ai_settings, screen, p1, p2, ball, play_button, stats, sb, fg)

run_game()
