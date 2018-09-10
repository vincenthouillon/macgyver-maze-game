#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Game in which MacGyver must pick up objects to lull a guardian to escape 
    the maze.
"""

from time import sleep

import pygame

from includes.classes import Maze
from includes.constants import (COLOR_BG, COLOR_FG, DISPLAY_SIZE, FONT,
                                ICON_GAME, IMG_MAC, OBJECTS, SPRITE_SIZE,
                                TITLE_WINDOW)
from includes.macgyver import MacGyver

# Initialization
pygame.init()
clock = pygame.time.Clock()

# variables
icon = pygame.image.load(ICON_GAME)
screen = pygame.display.set_mode(DISPLAY_SIZE)
loop = True
items = []

# Various settings
pygame.display.set_caption(TITLE_WINDOW)
pygame.display.set_icon(icon)
screen.fill(COLOR_BG)
pygame.key.set_repeat(200, 300)

# Instantiations
level = Maze()
macgyver = MacGyver(level)

img_mac = pygame.transform.scale(pygame.image.load(
    IMG_MAC).convert_alpha(), (SPRITE_SIZE, SPRITE_SIZE))

# Text display settings
item_font = pygame.font.Font(FONT, 18)
list_items = item_font.render(" items:" + str(items) + " ",
                              True, (COLOR_FG), (COLOR_BG))


def gameover_msg(text):
    """ To display the end-of-game message.

    Arguments:
        text {"text"} -- The message to display
    """

    gameover_background = pygame.Surface(screen.get_size())
    gameover_background.fill(COLOR_BG)
    screen.blit(gameover_background, (0, 0))
    # To display message
    gameover_font = pygame.font.Font(FONT, 48)
    game_over = gameover_font.render(
        text, True, (COLOR_FG), (COLOR_BG))
    # To center the text
    text_rect = game_over.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery
    screen.blit(game_over, (text_rect))


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

    level.display_maze(screen)
    screen.blit(img_mac, (macgyver.x, macgyver.y))
    screen.blit(list_items, (0, 422))
    pygame.display.flip()

    # region: Collision management
    if level.structure[macgyver.case_y][macgyver.case_x] == "neddle":
        level.structure[macgyver.case_y][macgyver.case_x] = " "
        items.append("neddle")
        list_items = item_font.render(
            " Items:" + str(items) + " ", True, (COLOR_FG), (COLOR_BG))

    if level.structure[macgyver.case_y][macgyver.case_x] == "ether":
        level.structure[macgyver.case_y][macgyver.case_x] = " "
        items.append("ether")
        list_items = item_font.render(
            " Items:" + str(items)+" ", True, (COLOR_FG), (COLOR_BG))

    if level.structure[macgyver.case_y][macgyver.case_x] == "tube":
        level.structure[macgyver.case_y][macgyver.case_x] = " "
        items.append("tube")
        list_items = item_font.render(
            " Items:" + str(items) + " ", True, (COLOR_FG), (COLOR_BG))

    if level.structure[macgyver.case_y][macgyver.case_x] == "e":
        if len(items) == len(OBJECTS):
            gameover_msg("You have won !!!")
            pygame.display.flip()
            sleep(2)
            loop = False
            pygame.quit()
        else:
            gameover_msg("Sorry, you lost :(")
            pygame.display.flip()
            sleep(2)
            loop = False
            pygame.quit()
    # endregion
