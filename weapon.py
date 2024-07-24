import math

import pygame.transform
from character import Character


class Weapon:
    def __init__(self, image):
        self.original_image = image
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()


    def update(self, hero: Character):
        self.rect.center = hero.rect.center

        # update the rotation angle
        mouse_pos = pygame.mouse.get_pos() # returns a tuple (x, y)
        x_dist = mouse_pos[0] - self.rect.centerx
        y_dist = -(mouse_pos[1] - self.rect.centery)
        self.angle = math.degrees(math.atan2(y_dist, x_dist))


    def draw(self, surface):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        surface.blit(self.image, (self.rect.x, self.rect.y))
