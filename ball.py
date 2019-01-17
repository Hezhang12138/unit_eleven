import pygame, block


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        self.color = color
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.radius = radius
        self.image = pygame.Surface((self.radius, self.radius))
        self.rect = self.image.get_rect()
        self.image.fill(self.color)
        self.speedx = 6
        self.speedy = 5


    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.speedy = -self.speedy
        if self.rect.left < 0 or self.rect.right > self.windowWidth:
            self.speedx = -self.speedx

    def collide(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.speedy = -self.speedy

    def collideBrick(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.speedy = -self.speedy


