import sys 
import pygame
from ship import Ship

def check_events(ship : Ship):
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # KEY DOWN 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        # KEY UP 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
        
     
        
        



def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    
    # Redraw the screen during each pass
    screen.fill(ai_settings.bg_color)
    ship.blitme()
       
    # Make the most recent drawn visible
    pygame.display.flip()
