import math
import random

import pygame.transform
from character import Character

import constants as const



class Weapon:
    def __init__(self, image, projectile_image):
        self.original_image = image
        self.projectile_image = projectile_image
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.fired = False
        self.last_fired = 0



    def update(self, hero: Character):
        arrow = None
        self.rect.center = hero.rect.center

        # update the rotation angle
        mouse_pos = pygame.mouse.get_pos() # returns a tuple (x, y)
        x_dist = mouse_pos[0] - self.rect.centerx
        y_dist = -(mouse_pos[1] - self.rect.centery)
        self.angle = math.degrees(math.atan2(y_dist, x_dist))
        if (pygame.mouse.get_pressed()[0] and not self.fired
                and (pygame.time.get_ticks() - self.last_fired) > const.ARROW_COOLDOWN_PERIOD):
            self.fired = True
            arrow = Arrow(self.projectile_image, self.rect.centerx, self.rect.centery, self.angle)
            self.last_fired = pygame.time.get_ticks()

        if not pygame.mouse.get_pressed()[0]:
            self.fired = False

        return arrow


    def draw(self, surface):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        surface.blit(self.image, (self.rect.x, self.rect.y))
        # pygame.draw.rect(surface, const.RED, self.rect, 1)

class Arrow(pygame.sprite.Sprite):

    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = image

        self.angle = angle
        self.image = pygame.transform.rotate(self.image, self.angle - 90)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # arrow speed
        self.dx = const.ARROW_SPEED * math.cos(math.radians(self.angle))
        self.dy = - const.ARROW_SPEED * math.sin(math.radians(self.angle))


    def update(self, enemy: Character):
        self.rect.x += self.dx
        self.rect.y += self.dy
        damage = 0


        # test if visible
        if self.rect.x < 0 or self.rect.x > const.SCREEN_WIDTH \
                or self.rect.y < 0 or self.rect.y > const.SCREEN_HEIGHT:
            self.kill()

        # test if hit enemy
        if self.rect.colliderect(enemy.rect) and enemy.health > 0:
            self.kill()
            damage = int(const.ARROW_MAX_DAMAGE * random.random())


        return damage


    def draw(self, surface):
        surface.blit(self.image, self.rect)
        # pygame.draw.rect(surface, const.WHITE, self.rect, 1)