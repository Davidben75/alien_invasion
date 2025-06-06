import sys 
import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien

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
            elif event.key == pygame.K_q:
                  sys.exit()
                              
def check_keyup_events(event ,ship : Ship):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen."""

    # Redraw the screen during each pass
    screen.fill(ai_settings.bg_color)

    # Redraw bullets
    for bullet in bullets.sprites():
         bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
       
    # Make the most recent drawn visible
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship ,aliens, bullets):
    bullets.update()

    # Get rid of bullets that disapperead 
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, ship ,aliens, bullets)

def check_bullet_alien_collision(ai_settings, screen, ship ,aliens, bullets): 
    # Check if a bullet hit an allien
    # If so get rid of both
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
     """Fire a bullet if the limit not reached"""
     if len(bullets) < ai_settings.bullets_allowed:
                    new_bullet = Bullet(ai_settings, screen, ship)
                    bullets.add(new_bullet)

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x    
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship,aliens):
    """ Create a full fleet of aliens"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):    
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens"""
    available_space_y = (ai_settings.screen_height - ( 3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of alien """ 
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width)) 
    return number_aliens_x    

def update_aliens(ai_settings, ship,aliens):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien and ship collision 
    if pygame.sprite.spritecollideany(ship, aliens):
         print("Ship hit!!!")

def check_fleet_edges(ai_settings, aliens):
     for alien in aliens.sprites():
          if alien.check_edges():
               change_fleet_direction(ai_settings, aliens)
               break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1