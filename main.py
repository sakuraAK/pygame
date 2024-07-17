import pygame
from pygame import mixer

from util import draw_text, scale_image
import constants as const
from character import Character

pygame.init()
mixer.init()


screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Crawler")
clock = pygame.time.Clock()


run = True

move_left = False
move_right = False
move_up = False
move_down = False

dx = 0
dy = 0



def draw_game_info():
    pass



def draw_level():
    pass


# image processing
hero_image = pygame.image.load("assets/images/dracula/idle/0.png")
hero_image = scale_image(hero_image, const.CHARACTER_SCALE)




# game objects

hero = Character(const.SCREEN_WIDTH // 2, const.SCREEN_HEIGHT // 2, hero_image)

draw_level()


while run:
    clock.tick(const.FPS)
    screen.fill(const.BG)

    # game logic

    # calculate player speed
    dx = 0
    dy = 0
    if move_right:
        dx = const.CHARACTER_SPEED
    if move_left:
        dx = -const.CHARACTER_SPEED
    if move_up:
        dy = -const.CHARACTER_SPEED
    if move_down:
        dy = const.CHARACTER_SPEED


    # move
    hero.move(dx, dy)

    # update
    hero.update()

    # draw
    hero.draw(screen)


    # event handling
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False


        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                move_left = True
            elif e.key == pygame.K_d:
                move_right = True
            elif e.key == pygame.K_w:
                move_up = True
            elif e.key == pygame.K_s:
                move_down = True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_a:
                move_left = False
            elif e.key == pygame.K_d:
                move_right = False
            elif e.key == pygame.K_w:
                move_up = False
            elif e.key == pygame.K_s:
                move_down = False



    pygame.display.update()


pygame.quit()