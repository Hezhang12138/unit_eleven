import pygame, sys
from pygame.locals import *
import brick
import paddle
import ball

def main():
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3

    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    color = [RED, ORANGE, YELLOW, GREEN, CYAN]
    mainSurface = pygame.display.set_mode((400, 600), 32, 0)


    background_image = pygame.image.load("background.jpg")
    background_rect = background_image.get_rect()
    background_rect.x = 0
    background_rect.y = 0
    bricks_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()
    x = 0
    y = BRICK_Y_OFFSET
    for a in color:
        for b in range(2):
            for c in range(BRICKS_PER_ROW):
                my_brick = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, a)
                bricks_group.add(my_brick)
                my_brick.rect.x = x
                my_brick.rect.y = y
                mainSurface.blit(my_brick.image, my_brick.rect)
                x = x +BRICK_WIDTH + BRICK_SEP
            y = y +BRICK_HEIGHT + BRICK_SEP
            x = 0

    paddle_1 = paddle.Paddle(mainSurface, WHITE, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle_1.rect.x = APPLICATION_WIDTH / 2 - 30
    paddle_1.rect.y = APPLICATION_HEIGHT - 30
    paddle_1.move()
    mainSurface.blit(paddle_1.image, paddle_1.rect)
    paddle_group.add(paddle_1)

    my_ball = ball.Ball(ORANGE, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
    my_ball.rect.x = APPLICATION_WIDTH / 2
    my_ball.rect.y = APPLICATION_HEIGHT / 2
    mainSurface.blit(my_ball.image, my_ball.rect)


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        mainSurface.blit(background_image, background_rect)
        for block in bricks_group:
            mainSurface.blit(block.image, block.rect)
        paddle_1.move()
        my_ball.move()
        my_ball.collide(paddle_group)
        my_ball.collideBrick(bricks_group)
        mainSurface.blit(paddle_1.image, paddle_1.rect)
        mainSurface.blit(my_ball.image, my_ball.rect)
        if my_ball.rect.bottom >= APPLICATION_HEIGHT:
            my_ball.rect.x = APPLICATION_WIDTH / 2
            my_ball.rect.y = APPLICATION_HEIGHT / 2
        pygame.display.update()


main()
