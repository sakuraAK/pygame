import math

import pygame
import constants as const
class Character:
    def __init__(self, x, y, image):
        self.rect = pygame.Rect(0, 0, const.CHARACTER_SIZE - 5, const.CHARACTER_SIZE + 17)
        self.rect.center = (x, y)
        self.image = image




    def move(self, dx, dy):

        # correct diagonal speed
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2)/2)
            dy = dy * (math.sqrt(2)/2)

        self.rect.x += dx
        self.rect.y += dy



    def update(self):
        pass


    def draw(self, surface):
        surface.blit(self.image, self.rect)
        pygame.draw.rect(surface, const.RED, self.rect, 1)