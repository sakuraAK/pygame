import pygame
from constants import RED, SCREEN_WIDTH, SCREEN_HEIGHT, PAD_WIDTH, BALL_WIDTH, BRICK_WIDTH, BRICK_HEIGHT, BRICK_HIT_CNT
from math import sqrt, ceil

class Pad:

    def __init__(self, image):
        self.rect = pygame.Rect(0, 0, PAD_WIDTH, 15)
        self.image = image
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 15)


    def move(self, dx):
        self.rect.x += dx

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - PAD_WIDTH:
            self.rect.x = SCREEN_WIDTH - PAD_WIDTH




    def draw(self, surface):
        surface.blit(self.image, self.rect)
        pygame.draw.rect(surface, RED, self.rect, 1)


class Ball:

    def __init__(self, image, x, y):
        self.image = image
        self.rect = pygame.Rect(x, y, BALL_WIDTH, BALL_WIDTH)
        self.dx = 2
        self.dy = 2


    def move(self, pad, bricks):

    #  detect collision with the pad
        if self.rect.colliderect(pad.rect):
            self.dy = -self.dy



    # detect go off the screen left

        if self.rect.x < 0:
            self.rect.x = 0
            self.dx = -self.dx

    # detect go off the screen right

        if self.rect.x > SCREEN_WIDTH - BALL_WIDTH:
            self.rect.x = SCREEN_WIDTH - BALL_WIDTH
            self.dx = -self.dx


        self.rect.y += self.dy
        for brick in bricks:
            if self.rect.colliderect(brick.rect):
                if self.dy < 0:
                    # hit brick from below
                    self.rect.top = brick.rect.bottom
                else:
                    self.rect.bottom = brick.rect.top
                self.dy = -self.dy
                brick.update_hit()

        self.rect.x += self.dx
        for brick in bricks:
            if self.rect.colliderect(brick.rect):
                if self.dx > 0:
                    #hit the brick from the left
                    self.rect.right = brick.rect.left
                else:
                    self.rect.left = brick.rect.right
                self.dx = -self.dx
                brick.update_hit()


    def draw(self, surface):
        surface.blit(self.image, self.rect)
        pygame.draw.rect(surface, RED, self.rect, 1)


class Brick(pygame.sprite.Sprite):
    def __init__(self, images, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.hit_counter = 0
        self.images = images
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)

    def draw(self, surface):
        surface.blit(self.images[self.hit_counter], self.rect)
        pygame.draw.rect(surface, RED, self.rect, 1)

    def update_hit(self):
        if self.hit_counter < BRICK_HIT_CNT:
            self.hit_counter += 1
        else:
            self.kill()
