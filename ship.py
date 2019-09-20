import pygame


class Ship:
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('Images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        r, sr = self.rect, self.screen_rect
        r.centerx = sr.centerx
        r.bottom = sr.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
