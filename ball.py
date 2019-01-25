import pygame, block


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        super().__init__()
        self.color = color
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.radius = radius
        self.image = pygame.Surface((self.radius, self.radius))
        self.rect = self.image.get_rect()
        self.image.fill(self.color)
        self.speedx = 10
        self.speedy = 24
        self.break_sound = pygame.mixer.Sound("baseball_hit.wav")
        self.paddle_sound = pygame.mixer.Sound("blurp_x.wav")

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
            self.paddle_sound.play()

    def collideBrick(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.speedy = -self.speedy
            self.break_sound.play()



