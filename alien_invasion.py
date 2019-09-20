import sys
import pygame
from settings import Settings
from ship import Ship

# PYTHON CRASH COURSE - Ch 12 has references for ship img, shooting bullets,


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.dims())
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(screen)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(settings.bg_color)
        ship.blitme()

        pygame.display.flip()
    sys.exit()


run_game()
