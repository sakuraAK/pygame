import pygame

def draw_text(font, text, color, pos_x, pos_y, surface):
    font_img = font.render(text, color, color)
    surface.blit(font_img, pygame.Rect(pos_x, pos_y, 40, 40))


def scale_image(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))
