import pygame, brick
from pygame.locals import *


pygame.init()
mainSurface = pygame.display.set_mode((500, 500), 32, 0)
pygame.display.set_caption("Bricks")
width =
bricks = brick.Brick(mainSurface, )
bricks.draw()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()