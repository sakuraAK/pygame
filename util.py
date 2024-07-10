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


class SingletonLogger(metaclass=SingletonMeta):
    _log_file = None

    def __init__(self, path):
        if self._log_file is None:
            self._log_file = open(path, 'w')

    def log(self, record):
        self._log_file.write(f'[{datetime.now()}] - [{record}]\n')

    def close_log(self):
        if self._log_file:
            self._log_file.close()
            self._log_file = None


if __name__ == "__main__":
    l1 = SingletonLogger("app.log")
    l1.log("Logging into l1")


    l2 = SingletonLogger("#####%.")
    l2.log("Logging into l2")

    l1.close_log()
    l2.close_log()
