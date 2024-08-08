import math

import pygame
import constants as const
class Character:
    """

    """
    def __init__(self, x, y, animation_list, character_type: int):
        """

        :param x:
        :param y:
        :param animation_list:
        :param character_type: value to identify the type of character. 1 - dracula
        """
        self.animation_list = animation_list[character_type - 1]
        self.character_type = character_type
        self.rect = pygame.Rect(0, 0, const.CHARACTER_SIZE, const.CHARACTER_SIZE)
        self.rect.center = (x, y)
        self.frame_idx = 0
        self.moving = False
        self.image = self.animation_list[1 if self.moving else 0][self.frame_idx]
        self.flipped = False
        self.image_last_update_time = pygame.time.get_ticks()
        if character_type == 1:
            self.health = 75
        else:
            self.health = 20
        self.score = 0





    def move(self, dx, dy, obstacles):

        # determine if moving
        self.moving = dx != 0 or dy != 0

        # determine if the image should be flipped

        if self.moving:
            self.flipped = dx > 0
        else:
            mouse_pos = pygame.mouse.get_pos()
        # if pointing weapon right then flip
            self.flipped = self.rect.centerx < mouse_pos[0]


        # correct diagonal speed
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2)/2)
            dy = dy * (math.sqrt(2)/2)

        self.rect.x += dx

        # detect collisions
        for tile in obstacles:
            rect = tile[1]
            if self.rect.colliderect(rect):
                if dx > 0:
                    self.rect.right = rect.left
                else:
                    self.rect.left = rect.right

        self.rect.y += dy
        for tile in obstacles:
            rect = tile[1]
            if self.rect.colliderect(rect):
                if dy > 0:
                    self.rect.bottom = rect.top
                else:
                    self.rect.top = rect.bottom

        # leaving screen
        # left
        if self.rect.left <= 0:
            self.rect.left = 0
        # right
        if self.rect.right >= const.SCREEN_WIDTH:
            self.rect.right = const.SCREEN_WIDTH
        # up
        if self.rect.top <= const.INFO_SECTION_HEIGHT:
            self.rect.top = const.INFO_SECTION_HEIGHT
        # down
        if self.rect.bottom >= const.SCREEN_HEIGHT:
            self.rect.bottom = const.SCREEN_HEIGHT

        # collision



    def update(self):
        if self.health > 0:
            current_time = pygame.time.get_ticks()
            if current_time - self.image_last_update_time > const.ANIMATION_COOLDOWN_PERIOD:
                self.frame_idx += 1
                if self.frame_idx >= len(self.animation_list[1 if self.moving else 0]):
                    self.frame_idx = 0
                self.image_last_update_time = current_time

            self.image = self.animation_list[1 if self.moving else 0][self.frame_idx]


    def draw(self, surface):
        flipped_image = pygame.transform.flip(self.image, self.flipped, False)
        surface.blit(flipped_image, self.rect)
        pygame.draw.rect(surface, const.RED, self.rect, 1)