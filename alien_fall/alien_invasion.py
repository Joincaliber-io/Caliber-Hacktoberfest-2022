import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from background import Background
import game_functions as gf
from alien import Alien
from pausescreen import PauseScreen

def run_game():
        # Initialize pygame, settings, and screen object.
        pygame.init()
        ai_settings = Settings()
        screen = pygame.display.set_mode(
                (ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #Make a ship, background object and pause_screen
        ship = Ship(ai_settings, screen)
        bg_obj = Background(screen)
        pause_screen = PauseScreen(screen)

        # Make a group to store bullets and aliens in.
        bullets = Group()
        aliens = Group()

        #Make a alien fleet
        gf.create_fleet(ai_settings, screen, ship, aliens)

        # Start the main loop for the game.
        while True:
                # Watch for keyboard and mouse events.
                gf.check_events(ai_settings, screen, ship, bullets)

                if(ai_settings.paused):
                        gf.pause_game(ai_settings, screen, pause_screen)
                else:
                        gf.update_bullets(ai_settings, screen, ship, aliens, bullets, bg_obj)
                        ship.update()
                        gf.update_aliens(ai_settings, aliens, screen, ship, bullets, bg_obj)
                        gf.update_screen(ai_settings, screen, ship, bg_obj, bullets, aliens)
run_game()
