import pygame
from constants import BG, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, OBJ_SPEED, BALL_SCALE, PANEL, WHITE, FONT_SIZE_MED, BLACK, \
GAME_INFO_SECTION_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, RED, FONT_SIZE_LARGE, FONT_SIZE_SMALL


from gameobjects import Pad, Ball, Brick, GameData, Button

from util import draw_text, scale_image


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()



new_game = True




def draw_game_info(game_data):
    pygame.draw.rect(screen, PANEL, (0, 0, SCREEN_WIDTH, GAME_INFO_SECTION_HEIGHT))
    pygame.draw.line(screen, WHITE, (0, GAME_INFO_SECTION_HEIGHT), (SCREEN_WIDTH, GAME_INFO_SECTION_HEIGHT))
    draw_text(atari_font_medium, f"Level:{game_data.level}", BLACK, SCREEN_WIDTH // 2 - 100, 10, screen)
    draw_text(atari_font_medium, f"Lives:{game_data.lives}", BLACK, 10, 10, screen)
    draw_text(atari_font_medium, f"Score:{game_data.score}", BLACK, SCREEN_WIDTH - 200, 10, screen)


def draw_game_over_screen(game_data: GameData):
    draw_text(atari_font_large, "Game Over!", RED, SCREEN_WIDTH // 2 - 230, 100, screen)
    draw_text(atari_font_large, "Game Over!", WHITE, SCREEN_WIDTH // 2 - 230, 103, screen)

    draw_text(atari_font_medium, f"Your score is: {game_data.score}", WHITE, SCREEN_WIDTH // 2 - 200, 200, screen)


    try_again_button = Button("Try Again", SCREEN_WIDTH // 2 - 150, 250, button_image, atari_font_small, WHITE)
    try_again_button.draw(screen)
    if try_again_button.get_pressed():
        game_data.reset()

def draw_main_menu_screen():
    draw_text(atari_font_medium, "Atari Breakout 1976", RED, SCREEN_WIDTH // 2 - 230, 100, screen)
    draw_text(atari_font_medium, "Atari Breakout 1976", WHITE, SCREEN_WIDTH // 2 - 230, 103, screen)

    easy_button = Button("Easy", SCREEN_WIDTH // 2 - 150, 150, button_image, atari_font_small, WHITE)
    easy_button.draw(screen)
    if easy_button.get_pressed():
        pass

    hard_button = Button("Hard", SCREEN_WIDTH // 2 - 150, 220, button_image, atari_font_small, WHITE)
    hard_button.draw(screen)
    if hard_button.get_pressed():
        pass

    insane_button = Button("Insane", SCREEN_WIDTH // 2 - 150, 290, button_image, atari_font_small, WHITE)
    insane_button.draw(screen)
    if insane_button.get_pressed():
        pass

    quit_button = Button("Quit", SCREEN_WIDTH // 2 - 150, 360, button_image, atari_font_small, WHITE)
    quit_button.draw(screen)
    if quit_button.get_pressed():
        pass




# image processing
pad_image = pygame.image.load("./assets/images/pad.png")
ball_image = scale_image(pygame.image.load("./assets/images/ball.png"), BALL_SCALE)
atari_font_small = pygame.font.Font("assets/fonts/AtariClassic.ttf", FONT_SIZE_SMALL)
atari_font_medium = pygame.font.Font("assets/fonts/AtariClassic.ttf", FONT_SIZE_MED)
atari_font_large = pygame.font.Font("assets/fonts/AtariClassic.ttf", FONT_SIZE_LARGE)
brick_image_whole = scale_image(pygame.image.load("./assets/images/1_0.png"), 0.25)
brick_image_cracked = scale_image(pygame.image.load("./assets/images/1_1.png"), 0.25)
brick_images = [brick_image_whole, brick_image_cracked]

button_image = scale_image(pygame.image.load("./assets/images/1_0.png"), 0.5)


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



game_data = GameData(1)

while run:
    clock.tick(FPS)
    screen.fill(BG)

    if new_game:
        draw_main_menu_screen()
    else:
#     game logic

        if not game_data.game_over:
            # calculate movement
            dx = 0
            if move_left:
                dx = -OBJ_SPEED
            if move_right:
                dx = OBJ_SPEED

            pad.move(dx)
            score_increment, off_screen = ball.move(pad, bricks)
            game_data.score += score_increment

            if off_screen:
                if game_data.lives == 0:
                    game_data.game_over = True
                else:
                    game_data.lives -= 1
                    ball = Ball(ball_image, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


            for brick in bricks:
                brick.draw(screen)

            # bricks.draw(screen)

            pad.draw(screen)
            ball.draw(screen)

            draw_game_info(game_data)
            # event handling
        else:
            #draw game over screen
            ball = Ball(ball_image, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            draw_game_over_screen(game_data)


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