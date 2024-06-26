import pygame
from constants import BG, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, OBJ_SPEED, BALL_SCALE, PANEL, WHITE, FONT_SIZE_MED, BLACK, \
GAME_INFO_SECTION_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT

from gameobjects import Pad, Ball, Brick



pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()

level = 1
score = 0
lives = 3

def scale_image(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))

def draw_text(font, text, color, pos_x, pos_y, surface):
    font_img = font.render(text, color, color)
    surface.blit(font_img, pygame.Rect(pos_x, pos_y, 40, 40))


def draw_game_info():
    pygame.draw.rect(screen, PANEL, (0, 0, SCREEN_WIDTH, GAME_INFO_SECTION_HEIGHT))
    pygame.draw.line(screen, WHITE, (0, GAME_INFO_SECTION_HEIGHT), (SCREEN_WIDTH, GAME_INFO_SECTION_HEIGHT))
    draw_text(atari_font_medium, f"Level:{level}", BLACK, SCREEN_WIDTH // 2 - 100, 10, screen)
    draw_text(atari_font_medium, f"Lives:{lives}", BLACK, 10, 10, screen)
    draw_text(atari_font_medium, f"Score:{score}", BLACK, SCREEN_WIDTH - 200, 10, screen)

# image processing
pad_image = pygame.image.load("./assets/images/pad.png")
ball_image = scale_image(pygame.image.load("./assets/images/ball.png"), BALL_SCALE)
atari_font_medium = pygame.font.Font("assets/fonts/AtariClassic.ttf", FONT_SIZE_MED)
brick_image_whole = scale_image(pygame.image.load("./assets/images/1_0.png"), 0.25)
brick_image_cracked = scale_image(pygame.image.load("./assets/images/1_1.png"), 0.25)
brick_images = [brick_image_whole, brick_image_cracked]

run = True
move_left = False
move_right = False
move_up = False
move_down = False

# game objects
pad = Pad(pad_image)
ball = Ball(ball_image, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
bricks = pygame.sprite.Group()

for i in range(SCREEN_WIDTH // BRICK_WIDTH):
    brick = Brick(brick_images, 0 + i * BRICK_WIDTH, GAME_INFO_SECTION_HEIGHT + 5)
    bricks.add(brick)




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
    ball.move(pad, bricks)

    for brick in bricks:
        brick.draw(screen)

    # bricks.draw(screen)

    pad.draw(screen)
    ball.draw(screen)

    draw_game_info()
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