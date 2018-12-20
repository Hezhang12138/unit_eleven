import pygame

class Paddle(pygame.sprite.Sprite):

    def __init__(self, main_surface, color, width, height):
        super().__init__()
        self.main_surface = main_surface
        self.width = width
        self.height = height
        self.color = color

        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.image.fill(self.color)

    def move(self):
        screen_width = self.main_surface.get_width()
        screen_height = self.main_surface.get_height()


