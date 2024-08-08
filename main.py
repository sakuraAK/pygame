import pygame
from pygame import mixer
import csv

from util import draw_text, scale_image, DamageText
import constants as const
from character import Character
from weapon import Weapon
from item import Item



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

level = 1

dx = 0
dy = 0


font = pygame.font.Font("assets/fonts/AtariClassic.ttf", const.FONT_SIZE_SMALL)


def draw_game_info(surface, coin_image, full_heart, half_empty_heart, empty_heart, player, coin):
    pygame.draw.rect(surface, const.PANEL, (0, 0, const.SCREEN_WIDTH, const.INFO_SECTION_HEIGHT))
    pygame.draw.line(surface, const.WHITE, (0, 40), (const.SCREEN_WIDTH, const.INFO_SECTION_HEIGHT))

    # level information
    draw_text(font, f"Level: {level}", const.BLACK, const.SCREEN_WIDTH // 2 - 40, 15, surface)

    # points display
    # rect = pygame.Rect(const.SCREEN_WIDTH - 80, 15, 20, 20)
    # surface.blit(coin_image, rect)

    coin.update(player)
    coin.draw(surface)

    draw_text(font, f"x{player.score}", const.BLACK, const.SCREEN_WIDTH - 65, 15, surface)

    # display character health
    number_of_hearts = const.HERO_HEALTH // 20
    for i in range(number_of_hearts):
        if player.health - (number_of_hearts - i - 1) * 20 >= 20:
            surface.blit(full_heart, (10 + 50 * i, 5))
        elif player.health - (number_of_hearts - i - 1) * 20 > 10:
            surface.blit(half_empty_heart, (10 + 50 * i, 5))
        else:
            surface.blit(empty_heart, (10 + 50 * i, 5))



def draw_level():
    pass


# image processing
characters = ["dracula", "zombie"]
actions = ["idle", "move"]
animation_list = []

for character in characters:
    character_animations = []
    for action in actions:
        action_animations = []
        for i in range(4):
            image = pygame.image.load(f"assets/images/{character}/{action}/{i}.png")
            image = scale_image(image, const.CHARACTER_SCALE)
            action_animations.append(image)
        character_animations.append(action_animations)
    animation_list.append(character_animations)

# add items animation list
items_animation_list = []
item_types = ["coin", "potion_red"]
for item_type in item_types:
    item_animation_list = []
    for i in range(4):
        item_image = scale_image(pygame.image.load(f"assets/images/items/{item_type}_f{i}.png"), const.ITEM_SCALE)
        item_animation_list.append(item_image)
    items_animation_list.append(item_animation_list)



bow_image = pygame.image.load("assets/images/weapons/bow.png")
bow_image = scale_image(bow_image, const.WEAPON_SCALE)

arrow_image = pygame.image.load("assets/images/weapons/arrow.png")
arrow_image = scale_image(arrow_image, const.WEAPON_SCALE)

coin_image = scale_image(pygame.image.load("assets/images/items/coin_f0.png"), const.ITEM_SCALE)
full_heart_image = scale_image(pygame.image.load("assets/images/items/heart_full.png"), const.ITEM_SCALE)
half_empty_heart_image = scale_image(pygame.transform.flip(pygame.image.load("assets/images/items/heart_half.png"), True, False), const.ITEM_SCALE)
empty_heart_image = scale_image(pygame.image.load("assets/images/items/heart_empty.png"), const.ITEM_SCALE)

# map tiles

tiles_images = []
for i in range(18):
    tiles_images.append(scale_image(pygame.image.load(f"assets/images/tiles/{i}.png"), const.MAP_TILE_SCALE))



# game objects

hero = Character(const.SCREEN_WIDTH // 2, const.SCREEN_HEIGHT // 2, animation_list, 1)
weapon = Weapon(bow_image, arrow_image)
enemy = Character(100, const.SCREEN_HEIGHT // 2, animation_list, 2)

info_coin = Item(const.SCREEN_WIDTH - 80, 22, 0, items_animation_list)




draw_level()

arrows = pygame.sprite.Group()
damage_text_grp = pygame.sprite.Group()
items_group = pygame.sprite.Group()
items_group.add(Item(80, 80, 0, items_animation_list))
items_group.add(Item(100, 100, 1, items_animation_list))



# generate a map
tile_data = []
for i in range(150):
    row = [-1] * 150
    tile_data.append(row)

with open(f"assets/levels/level{level}_data.csv") as in_f:
    tile_data_raw = csv.reader(in_f, delimiter=",")
    for i, row in enumerate(tile_data_raw):
        for j, tile in enumerate(row):
            tile_data[i][j] = int(tile)


map_tiles = []
wall_tiles = []

for i, row in enumerate(tile_data):
    for j, tile_number in enumerate(row):
        if tile_number < 0:
            continue
        image = tiles_images[tile_number]
        image_rec = image.get_rect()
        image_y = i * const.TILE_SIZE
        image_x = j * const.TILE_SIZE
        image_rec.center = (image_x, image_y)

        tile = [image, image_rec, image_x, image_y]
        if tile_number == 7:
            wall_tiles.append(tile)

        map_tiles.append(tile)


while run:
    clock.tick(const.FPS)
    screen.fill(const.BG)

    draw_game_info(screen, coin_image, full_heart_image, half_empty_heart_image, empty_heart_image, hero, info_coin)

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
    hero.move(dx, dy, wall_tiles)

    # update
    hero.update()
    arrow = weapon.update(hero)
    if arrow:
        arrows.add(arrow)

    for arrow in arrows:
        damage = arrow.update(enemy)
        if damage > 0:
            enemy.health -= damage
            damage_text = DamageText(str(damage), enemy.rect.centerx, enemy.rect.centery, font)
            damage_text_grp.add(damage_text)

    enemy.update()
    damage_text_grp.update()
    items_group.update(hero)

    # draw section
    # draw tiles
    for tile_data in map_tiles:
        screen.blit(tile_data[0], tile_data[1])

    hero.draw(screen)
    weapon.draw(screen)
    arrows.draw(screen)
    enemy.draw(screen)

    for dt in damage_text_grp:
        dt.draw(screen)

    items_group.draw(screen)




    # coin.draw(screen)
    # potion.draw(screen)

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