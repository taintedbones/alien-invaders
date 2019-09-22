import pygame


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.dimensions = 1200, 700
        self.bg_color = pygame.Color('#404040')

        # Ship settings
        self.ship_speed_factor = 7.0

        # Bullet settings
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255

    def dims(self):
        return self.dimensions
