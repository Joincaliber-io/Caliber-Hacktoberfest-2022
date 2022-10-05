import sys
import pygame

def check_keydown_events(event, p1, p2, stats, ball):
    """Respond to key presses"""
    if event.key == pygame.K_UP:
        p1.moving_up = True
    elif event.key == pygame.K_DOWN:
        p1.moving_down = True

    if event.key == pygame.K_w:
        p2.moving_up = True
    elif event.key == pygame.K_s:
        p2.moving_down = True

    if event.key == pygame.K_q:
        sys.exit()

    if event.key == pygame.K_SPACE:
        if not stats.game_active:
            # Hide the cursor.
            pygame.mouse.set_visible(False)
            stats.game_active = True
            stats.game_end = False

    if event.key == pygame.K_LEFT:
        p1.up_hitter = True
        p1.down_hitter = False

    if event.key == pygame.K_RIGHT:
        p1.up_hitter = False
        p1.down_hitter = True

    if event.key == pygame.K_d:
        p2.up_hitter = True
        p2.down_hitter = False

    if event.key == pygame.K_a:
        p2.up_hitter = False
        p2.down_hitter = True
        

def check_keyup_events(event, p1, p2):
    """Respond to key releases"""
    if event.key == pygame.K_UP:
        p1.moving_up = False
    elif event.key == pygame.K_DOWN:
         p1.moving_down = False

    if event.key == pygame.K_w:
        p2.moving_up = False
    elif event.key == pygame.K_s:
        p2.moving_down = False
    

def check_events(p1, p2, stats, play_button, ball, screen):
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, p1, p2, stats, ball)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, p1, p2)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, ball, screen)

def check_play_button(stats, play_button, mouse_x, mouse_y, ball, screen):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Hide the cursor.
        pygame.mouse.set_visible(False)
        stats.game_active = True
        stats.game_end = False

def update_screen(ai_settings, screen, p1, p2, ball, play_button, stats, sb, fg):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Draw the score information
    sb.show_score()
    p1.blitme()
    p2.blitme()
    ball.blitme()
    
    if not stats.game_active and stats.game_end:
        fg.blitme()

    # Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    #Make the most recently drawn screen visible.
    pygame.display.flip()
