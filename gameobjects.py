import pygame
from constants import RED, SCREEN_WIDTH, SCREEN_HEIGHT, PAD_WIDTH, BALL_WIDTH, BRICK_WIDTH, BRICK_HEIGHT, BRICK_HIT_CNT, \
    BUTTON_WIDTH, BUTTON_HEIGHT, GAME_INFO_SECTION_HEIGHT
from math import sqrt, ceil

from util import draw_text, SingletonMeta

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

    def __init__(self, image, x, y, speed, wall_sound, brick_sound, pad_sound):
        self.image = image
        self.rect = pygame.Rect(x, y, BALL_WIDTH, BALL_WIDTH)
        self.dx = speed
        self.dy = speed
        self.wall_sound = wall_sound
        self.brick_sound = brick_sound
        self.pad_sound = pad_sound


    def move(self, pad, bricks):
        hit_counter = 0
        off_screen = False
        next_level = False

        if self.rect.y < GAME_INFO_SECTION_HEIGHT:
            next_level = True

        if self.rect.y > SCREEN_HEIGHT:
            # ball dropped out
            off_screen = True

        if not off_screen:
            #  detect collision with the pad
            if self.rect.colliderect(pad.rect):
                self.dy = -self.dy
                self.pad_sound.play()


            # detect go off the screen left

            if self.rect.x < 0:
                self.rect.x = 0
                self.dx = -self.dx
                self.wall_sound.play()

            # detect go off the screen right

            if self.rect.x > SCREEN_WIDTH - BALL_WIDTH:
                self.rect.x = SCREEN_WIDTH - BALL_WIDTH
                self.dx = -self.dx
                self.wall_sound.play()

            self.rect.y += self.dy
            for brick in bricks:
                if self.rect.colliderect(brick.rect):
                    hit_counter += 1
                    if self.dy < 0:
                        # hit brick from below
                        self.rect.top = brick.rect.bottom
                    else:
                        self.rect.bottom = brick.rect.top
                    self.dy = -self.dy
                    brick.update_hit()
                    self.brick_sound.play()

            self.rect.x += self.dx
            for brick in bricks:
                if self.rect.colliderect(brick.rect):
                    hit_counter += 1
                    if self.dx > 0:
                        #hit the brick from the left
                        self.rect.right = brick.rect.left
                    else:
                        self.rect.left = brick.rect.right
                    self.dx = -self.dx
                    brick.update_hit()
                    self.brick_sound.play()

        return hit_counter, off_screen, next_level

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



class GameData(metaclass=SingletonMeta):
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.level = 1
        self.ball_speed = 2
        self.game_over = False
        self.new_game = True
        self.run = True
        self.player_name = ""

    def reset(self):
        self.score = 0
        self.lives = 3
        self.level = 1
        self.game_over = False
        self.new_game = True
        self.player_name = ""

    def set_difficulty_level(self, difficulty):
        if difficulty == 2:
            self.lives = 2
            self.ball_speed = 3
        elif difficulty == 3:
            self.lives = 1
            self.ball_speed = 5


class Button:

    def __init__(self, text, x, y, image, font, font_color):
        self.rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.image = image
        self.text = text
        self.font = font
        self.font_color = font_color

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        draw_text(self.font, self.text, self.font_color, self.rect.centerx - 70, self.rect.centery, surface)


    def get_pressed(self):
        if pygame.mouse.get_pressed()[0]:
            return self.rect.collidepoint(pygame.mouse.get_pos())

