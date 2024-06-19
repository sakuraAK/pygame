import pygame
from constants import BG, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, OBJ_SPEED
from gameobjects import Pad



pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()

# image processing
pad_image = pygame.image.load("./assets/images/pad.png")


run = True
move_left = False
move_right = False
move_up = False
move_down = False

pad = Pad(pad_image)



while run:
    clock.tick(FPS)
    screen.fill(BG)

#     game logic

    # calculate movement
    dx = 0
    if move_left:
        dx = -OBJ_SPEED
    if move_right:
        dx = OBJ_SPEED

    pad.move(dx)

    pad.draw(screen)

    # event handling

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                move_left = True
            elif e.key == pygame.K_d:
                move_right = True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_a:
                move_left = False
            elif e.key == pygame.K_d:
                move_right = False



    pygame.display.update()


pygame.quit()