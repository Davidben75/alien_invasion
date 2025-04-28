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

    # Start the main loop
    while True:
        gf.check_events(ai_settings, screen ,ship, bullets)
        ship.update()
        bullets.update()

        # Get rid of bullets that disapperead 
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()