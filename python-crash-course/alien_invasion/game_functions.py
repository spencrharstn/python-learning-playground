import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""

    # Redraw the screen and ship during each pass through the loop
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets, ai_settings):
    """Update the position of the bullets and delete old bullets"""

    # Update bullet position
    bullets.update()

    # Get rid of old bullets
    for bullet in bullets.copy():
        if bullet.rect.left >= ai_settings.screen_width: 
            bullets.remove(bullet)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses"""

    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """Respond to key releases."""

    if event.key == pygame.K_UP:
        ship.moving_up = False
        # print_ship_location(ship)
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
        # print_ship_location(ship)    

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit isn't reached"""

    # Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

# def print_ship_location(ship):
#     """Prints the coordinates of the ship to console"""
#     print("X: {} Y: {}".format(ship.rect.x, ship.rect.y))
#     print("Center: {}".format(ship.center))
