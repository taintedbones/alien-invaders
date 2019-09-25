import sys
import pygame

import game_function as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group

# PYTHON CRASH COURSE - Ch 12 has references for ship img, shooting bullets,


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.dims())
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(screen, settings)
    bullets = Group()

    game_over = False
    while not game_over:
        game_over = gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(settings, screen, ship, bullets)

        screen.fill(settings.bg_color)
        ship.blitme()

        # pygame.display.flip()
    sys.exit()


run_game()
