#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Game in which MacGyver must pick up objects to lull a guardian to escape 
    the maze.

"""

from time import sleep

import pygame

from classes import Maze
from constants import (COLOR_BG, COLOR_FG, DISPLAY_SIZE, ICON_GAME, IMG_MAC,
                       OBJECTS, SPRITE_SIZE, TITLE_WINDOW)
from macgyver import MacGyver

# Initialization
pygame.init()
clock = pygame.time.Clock()

# variables
icon = pygame.image.load(ICON_GAME)
screen = pygame.display.set_mode(DISPLAY_SIZE)
items = []

# Various settings
pygame.display.set_caption(TITLE_WINDOW)
pygame.display.set_icon(icon)
pygame.key.set_repeat(200, 300)

# Instantiations
level = Maze()
macgyver = MacGyver(level)

img_mac = pygame.transform.scale(pygame.image.load(
    IMG_MAC).convert_alpha(), (SPRITE_SIZE, SPRITE_SIZE))

# Text display settings
item_font = pygame.font.SysFont("consolas", 18, bold=1)
list_items = item_font.render("items:" + str(items),
                              True, (COLOR_FG), (COLOR_BG))
end_font = pygame.font.SysFont("consolas", 48, bold=1)


loop = True

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and \
                event.key == pygame.K_ESCAPE:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                macgyver.move("right")
            elif event.key == pygame.K_LEFT:
                macgyver.move("left")
            if event.key == pygame.K_UP:
                macgyver.move("up")
            if event.key == pygame.K_DOWN:
                macgyver.move("down")

            # Collision management
            if level.structure[macgyver.case_y][macgyver.case_x] == "e":
                if len(items) == len(OBJECTS):
                    win_msg = " You have won !!! "
                    end_game = end_font.render(
                        win_msg, True, (COLOR_FG), (COLOR_BG))
                    screen.blit(end_game, (0, 160))
                    pygame.display.update()
                    sleep(3)
                    loop = False

                else:
                    print(f"Game Over {sorted(items)} != {sorted(OBJECTS)}")
                    lose_msg = "   You lost !!!   "
                    end_game = end_font.render(
                        lose_msg, True, (COLOR_FG), (COLOR_BG))
                    screen.blit(end_game, (0, 160))
                    pygame.display.update()
                    sleep(3)
                    loop = False

            if level.structure[macgyver.case_y][macgyver.case_x] == "neddle":
                level.structure[macgyver.case_y][macgyver.case_x] = " "
                items.append("neddle")
                list_items = item_font.render(
                    f"Items:" + str(items), True, (COLOR_FG), (COLOR_BG))

            if level.structure[macgyver.case_y][macgyver.case_x] == "ether":
                level.structure[macgyver.case_y][macgyver.case_x] = " "
                items.append("ether")
                list_items = item_font.render(
                    "Items:" + str(items), True, (COLOR_FG), (COLOR_BG))

            if level.structure[macgyver.case_y][macgyver.case_x] == "tube":
                level.structure[macgyver.case_y][macgyver.case_x] = " "
                items.append("tube")
                list_items = item_font.render(
                    "Items:" + str(items), True, (COLOR_FG), (COLOR_BG))

        level.display_maze(screen)
        screen.blit(img_mac, (macgyver.x, macgyver.y))
        screen.blit(list_items, (30, 426))

        pygame.display.flip()
        clock.tick(30)  # 30 fps

pygame.quit()
