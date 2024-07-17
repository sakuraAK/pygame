import pygame
from pygame import mixer

from util import draw_text, scale_image
import constants as const

pygame.init()
mixer.init()

# pygame.mixer.music.load("assets/audio/music.wav")
# pygame.mixer.music.set_volume(0.1)
# pygame.mixer.music.play(-1, 0.0, 5000)
#
# # load sounds
# brick_hit_sound = pygame.mixer.Sound("assets/audio/BrickHit.wav")
# brick_hit_sound.set_volume(0.5)
#
# wall_hit_sound = pygame.mixer.Sound("assets/audio/WallBounce.wav")
# wall_hit_sound.set_volume(0.5)
#
# pad_hit_sound = pygame.mixer.Sound("assets/audio/PadBounce.wav")
# pad_hit_sound.set_volume(0.5)

screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Crawler")
clock = pygame.time.Clock()


run = True

move_left = False
move_right = False
move_up = False
move_down = False




def draw_game_info():
    pass
    # data = GameData()
    # pygame.draw.rect(screen, PANEL, (0, 0, SCREEN_WIDTH, GAME_INFO_SECTION_HEIGHT))
    # pygame.draw.line(screen, WHITE, (0, GAME_INFO_SECTION_HEIGHT), (SCREEN_WIDTH, GAME_INFO_SECTION_HEIGHT))
    # draw_text(atari_font_medium, f"Level:{data.level}", BLACK, SCREEN_WIDTH // 2 - 100, 10, screen)
    # draw_text(atari_font_medium, f"Lives:{data.lives}", BLACK, 10, 10, screen)
    # draw_text(atari_font_medium, f"Score:{data.score}", BLACK, SCREEN_WIDTH - 200, 10, screen)




def draw_level():
    pass


# image processing





# game objects


draw_level()


while run:
    clock.tick(const.FPS)
    screen.fill(const.BG)

    # game logic

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