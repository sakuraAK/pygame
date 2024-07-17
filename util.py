import pygame
from datetime import datetime
def draw_text(font, text, color, pos_x, pos_y, surface):
    font_img = font.render(text, color, color)
    surface.blit(font_img, pygame.Rect(pos_x, pos_y, 40, 40))


def scale_image(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

