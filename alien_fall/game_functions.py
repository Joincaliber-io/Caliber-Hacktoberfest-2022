import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
        if event.key == pygame.K_RIGHT:
                ship.moving_right = True
                
        elif event.key == pygame.K_LEFT:
                ship.moving_left = True
                
        elif event.key == pygame.K_z:
                fire_bullet(ai_settings, screen, ship, bullets)
        elif event.key == pygame.K_p:
                if ai_settings.paused:
                        ai_settings.paused = False
                else:
                        ai_settings.paused = True
            

        elif event.key == pygame.K_q:
                sys.exit()

def check_keyup_events(event, ship, ai_settings):
        if event.key == pygame.K_RIGHT:
                ship.moving_right = False

        elif event.key == pygame.K_LEFT:
                ship.moving_left = False

        elif event.key == pygame.K_z:
                if ai_settings.aliens_defeted:
                    ship.image = pygame.image.load('images/angry_man2.bmp')
        elif ai_settings.aliens_defeted == False:
                ship.image = pygame.image.load('images/angry_man.bmp')


def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship, ai_settings)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""

    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        if ai_settings.aliens_defeted:
            ship.image = pygame.image.load('images/angry_man_shoting2.bmp')
        elif ai_settings.aliens_defeted == False:
            ship.image = pygame.image.load('images/angry_man_shoting.bmp')
        


def update_screen(ai_settings, screen, ship, bg_obj, bullets, aliens):
    """Update images on the screen and flip to the new screen."""
    #Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    bg_obj.blitme()

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    aliens.draw(screen)
    ship.blitme()
        

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def pause_game(ai_settings, screen, pause_screen):
    screen.fill(ai_settings.bg_color)
    pause_screen.blitme()
    
    pygame.display.flip()

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - 
        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number, ship):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen, ship)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)    

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
        # Create an alien and find the number of aliens in a row.

    alien = Alien(ai_settings, screen, ship)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)


    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number, ship)

def update_aliens(ai_settings, aliens, screen, ship, bullets, bg_obj):
    """
    Check if the fleet is at an edge,
        and then update the postions of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens, screen, ship, bullets, bg_obj)
    aliens.update()


def check_fleet_edges(ai_settings, aliens, screen, ship, bullets, bg_obj):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
        if alien.check_bottom():
            restart_game(ai_settings, aliens, screen, ship, bullets, bg_obj)
                    
            

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_bullets(ai_settings, screen, ship, aliens, bullets, bg_obj):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet.
        bullets.empty()
        bg_obj.ground_image = pygame.image.load('images/bg_image2.bmp')
        ai_settings.bg_color = (13, 36, 89)
        ship.image = pygame.image.load('images/angry_man2.bmp')
        ai_settings.aliens_defeted = True
        ai_settings.alien_speed_factor += 0.3
        
        create_fleet(ai_settings, screen, ship, aliens)

        for alien in aliens.sprites():
            alien.image = pygame.image.load('images/alien2.bmp')

def restart_game(ai_settings, aliens, screen, ship, bullets, bg_obj):
        bullets.empty()
        aliens.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        if ai_settings.aliens_defeted == True:
               ai_settings.aliens_defeted = False
               bg_obj.ground_image = pygame.image.load('images/bg_image.bmp')
               ai_settings.bg_color = (150,150,245)
               ai_settings.alien_speed_factor = ai_settings.alien_default_speed
               ship.image = pygame.image.load('images/angry_man.bmp')
               for alien in aliens.sprites():
                       alien.image = pygame.image.load('images/alien.bmp')
