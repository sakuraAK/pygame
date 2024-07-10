import pygame
from constants import BG, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, OBJ_SPEED, BALL_SCALE, PANEL, WHITE, FONT_SIZE_MED, BLACK, \
GAME_INFO_SECTION_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, RED, FONT_SIZE_LARGE, FONT_SIZE_SMALL, EASY, HARD, INSANE


from gameobjects import Pad, Ball, Brick, GameData, Button

from util import draw_text, scale_image


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()

game_data = GameData()


# new_game = False
# run = True
move_left = False
move_right = False
move_up = False
move_down = False

recording_name = False


def draw_game_info():
    data = GameData()
    pygame.draw.rect(screen, PANEL, (0, 0, SCREEN_WIDTH, GAME_INFO_SECTION_HEIGHT))
    pygame.draw.line(screen, WHITE, (0, GAME_INFO_SECTION_HEIGHT), (SCREEN_WIDTH, GAME_INFO_SECTION_HEIGHT))
    draw_text(atari_font_medium, f"Level:{data.level}", BLACK, SCREEN_WIDTH // 2 - 100, 10, screen)
    draw_text(atari_font_medium, f"Lives:{data.lives}", BLACK, 10, 10, screen)
    draw_text(atari_font_medium, f"Score:{data.score}", BLACK, SCREEN_WIDTH - 200, 10, screen)


def draw_game_over_screen():
    data = GameData()
    draw_text(atari_font_large, "Game Over!", RED, SCREEN_WIDTH // 2 - 230, 100, screen)
    draw_text(atari_font_large, "Game Over!", WHITE, SCREEN_WIDTH // 2 - 230, 103, screen)

    draw_text(atari_font_medium, f"Your score is: {data.score}", WHITE, SCREEN_WIDTH // 2 - 200, 200, screen)

    draw_text(atari_font_medium, f"Please enter your name:", WHITE, SCREEN_WIDTH // 2 - 270, 250, screen)
    draw_text(atari_font_medium, f"{'_' if data.player_name == '' else data.player_name}", WHITE, SCREEN_WIDTH // 2 - 100, 280, screen)
    # try_again_button = Button("Try Again", SCREEN_WIDTH // 2 - 150, 250, button_image, atari_font_small, WHITE)
    # try_again_button.draw(screen)
    # if try_again_button.get_pressed():
    #     data.reset()

def draw_high_score_screen():
    data = GameData()

    # print high score table
    draw_text(atari_font_medium, "Breakout Hall of Fame", WHITE, SCREEN_WIDTH // 2 - 230, 100, screen)

    results = get_results()
    cnt = 0
    for k, v in results.items():
        draw_text(atari_font_medium, f"{k} {'.'* (33 - len(k))} {v}", WHITE, 100, 130 + 40 * cnt, screen)
        cnt = 0

    try_again_button = Button("Try Again", 60, SCREEN_HEIGHT - 80, button_image, atari_font_small, WHITE)
    try_again_button.draw(screen)
    if try_again_button.get_pressed():
        data.reset()

    quit_button = Button("Quit", SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT - 80, button_image, atari_font_small, WHITE)
    quit_button.draw(screen)
    if quit_button.get_pressed():
        data.run = False

def draw_main_menu_screen():
    data = GameData()
    draw_text(atari_font_medium, "Atari Breakout 1976", RED, SCREEN_WIDTH // 2 - 230, 100, screen)
    draw_text(atari_font_medium, "Atari Breakout 1976", WHITE, SCREEN_WIDTH // 2 - 230, 103, screen)

    easy_button = Button("Easy", SCREEN_WIDTH // 2 - 130, 150, button_image, atari_font_small, WHITE)
    easy_button.draw(screen)
    if easy_button.get_pressed():
        data.new_game = False

    hard_button = Button("Hard", SCREEN_WIDTH // 2 - 130, 220, button_image, atari_font_small, WHITE)
    hard_button.draw(screen)
    if hard_button.get_pressed():
        data.set_difficulty_level(HARD)
        data.new_game = False

    insane_button = Button("Insane", SCREEN_WIDTH // 2 - 130, 290, button_image, atari_font_small, WHITE)
    insane_button.draw(screen)
    if insane_button.get_pressed():
        data.set_difficulty_level(INSANE)
        data.new_game = False

    quit_button = Button("Quit", SCREEN_WIDTH // 2 - 130, 360, button_image, atari_font_small, WHITE)
    quit_button.draw(screen)
    if quit_button.get_pressed():
        data.run = False

def draw_level():
    with open(f"./assets/levels/{game_data.level}.txt", 'r') as f_in:
        line = f_in.readline()
        line_cnt = 0
        while line:
            brick_type_list = line.split(",")
            cnt = 0
            for brick_type in brick_type_list:
                if int(brick_type) > 0:
                    brick = Brick(brick_images[int(brick_type) - 1], 0 + cnt * BRICK_WIDTH, GAME_INFO_SECTION_HEIGHT + 5 + BRICK_HEIGHT * line_cnt)
                    bricks.add(brick)
                cnt += 1
            line_cnt += 1
            line = f_in.readline()


# image processing
pad_image = pygame.image.load("./assets/images/pad.png")
ball_image = scale_image(pygame.image.load("./assets/images/ball.png"), BALL_SCALE)
atari_font_small = pygame.font.Font("assets/fonts/AtariClassic.ttf", FONT_SIZE_SMALL)
atari_font_medium = pygame.font.Font("assets/fonts/AtariClassic.ttf", FONT_SIZE_MED)
atari_font_large = pygame.font.Font("assets/fonts/AtariClassic.ttf", FONT_SIZE_LARGE)


brick_images = []
for i in range(4):
    brick_image_whole = scale_image(pygame.image.load(f"./assets/images/{i + 1}_0.png"), 0.25)
    brick_image_cracked = scale_image(pygame.image.load(f"./assets/images/{i + 1}_1.png"), 0.25)
    brick_images.append([brick_image_whole, brick_image_cracked])



button_image = scale_image(pygame.image.load("./assets/images/1_0.png"), 0.5)




# game objects
pad = Pad(pad_image)
ball = None
bricks = pygame.sprite.Group()

draw_level()

# for i in range(SCREEN_WIDTH // BRICK_WIDTH):
#     brick = Brick(brick_images, 0 + i * BRICK_WIDTH, GAME_INFO_SECTION_HEIGHT + 5)
#     bricks.add(brick)



def update_results():
    data = GameData()
    with open("results.txt", 'a') as out_file:
        out_file.write(f"{data.player_name},{data.score}\n")

def get_results():
    with open("results.txt", 'r') as in_file:
        line = in_file.readline()
        results = {}
        while line:
            line_parts = line.split(",")
            if not line_parts[0] in results or results[line_parts[0]] < line_parts[1]:
                results[line_parts[0]] = line_parts[1]
            line = in_file.readline()

    result_list = sorted(results.items(), key=lambda item: item[1])[::-1]
    return dict(result_list[:max(len(result_list), 4)])


while game_data.run:
    clock.tick(FPS)
    screen.fill(BG)

    if game_data.new_game:
        draw_main_menu_screen()
    else:
#     game logic
        if ball is None:
            ball = Ball(ball_image, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, game_data.ball_speed)

        if not game_data.game_over:
            # calculate movement
            dx = 0
            if move_left:
                dx = -OBJ_SPEED
            if move_right:
                dx = OBJ_SPEED

            pad.move(dx)
            score_increment, off_screen, next_level = ball.move(pad, bricks)
            game_data.score += score_increment

            if next_level:
                game_data.level += 1
                pad = Pad(pad_image)
                ball = None
                bricks = pygame.sprite.Group()
                draw_level()

            if off_screen:
                if game_data.lives == 0:
                    ball = None
                    game_data.game_over = True
                    recording_name = True
                else:
                    game_data.lives -= 1
                    ball = Ball(ball_image, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, game_data.ball_speed)

            for brick in bricks:
                brick.draw(screen)


            pad.draw(screen)

            if ball:
                ball.draw(screen)

            draw_game_info()
            # event handling
        elif recording_name:
            #draw game over screen
            # ball = Ball(ball_image, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, game_data.ball_speed)
            draw_game_over_screen()
        else:
            draw_high_score_screen()


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game_data.run = False


        if recording_name:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    recording_name = False
                    # update results
                    update_results()
                else:
                    if e.key >= 97 and e.key <= 122:
                        #small letters
                        game_data.player_name += chr(e.key)

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