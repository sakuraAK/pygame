import pygame
from datetime import datetime
import constants as const

def draw_text(font, text, color, pos_x, pos_y, surface):
    font_img = font.render(text, color, color)
    surface.blit(font_img, pygame.Rect(pos_x, pos_y, 40, 40))


def scale_image(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))


class DamageText(pygame.sprite.Sprite):

    def __init__(self, text, x, y, font):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.x = x
        self.y = y
        self.original_y = y
        self.font = font
        self.last_update = pygame.time.get_ticks()



    def update(self):
        if pygame.time.get_ticks() - self.last_update > const.DAMAGE_TEXT_COOLDOWN_PERIOD:
            self.y -= 5
            self.last_update = pygame.time.get_ticks()
        if self.original_y - self.y > 150:
            self.kill()
    def draw(self, surface):
        draw_text(self.font, self.text, const.RED, self.x, self.y, surface)

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

