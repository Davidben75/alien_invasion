import sys 
import pygame
from ship import Ship
from bullet import Bullet

def check_events(ai_settings, screen ,ship : Ship, bullets):
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # KEY DOWN 
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen,ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen ,ship : Ship, bullets):
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_SPACE:
                  fire_bullet(ai_settings, screen, ship, bullets)
                              
def check_keyup_events(event ,ship : Ship):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""

    # Redraw the screen during each pass
    screen.fill(ai_settings.bg_color)

    # Redraw bullets
    for bullet in bullets.sprites():
         bullet.draw_bullet()

    ship.blitme()
       
    # Make the most recent drawn visible
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()

def fire_bullet(ai_settings, screen, ship, bullets):
     """Fire a bullet if the limit not reached"""
     if len(bullets) < ai_settings.bullets_allowed:
                    new_bullet = Bullet(ai_settings, screen, ship)
                    bullets.add(new_bullet)
     