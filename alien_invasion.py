import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf

def run_game():
    # Initialize game
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.title)

    # Make a ship 
    ship = Ship(ai_settings ,screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship ,aliens)

    # Start the main loop
    while True:
        gf.check_events(ai_settings, screen ,ship, bullets)
        ship.update()
        bullets.update()

        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, ship ,aliens)
        gf.update_screen(ai_settings, screen, ship, aliens,bullets)

run_game()