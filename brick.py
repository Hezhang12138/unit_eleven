import pygame

class Brick(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        super().__init__()
        self.height = height
        self.width = width
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.color = color
        self.image.fill(self.color)