import pygame
from constants import RED, SCREEN_WIDTH, SCREEN_HEIGHT, PAD_WIDTH
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
        # pygame.draw.rect(surface, RED, self.rect, 1)