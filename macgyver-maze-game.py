#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Game in which MacGyver must pick up objects to lull a guardian to escape 
    the maze.

"""

import pygame

from classes import Maze
from macgyver import MacGyver
from constants import DISPLAY_SIZE, ICON_GAME, TITLE_WINDOW, IMG_MAC

# Initialization
pygame.init()
clock = pygame.time.Clock()

# variables
icon = pygame.image.load(ICON_GAME)
screen = pygame.display.set_mode(DISPLAY_SIZE)
bg_color = (173, 159, 146)

# Various settings
pygame.display.set_caption(TITLE_WINDOW)
pygame.display.set_icon(icon)
pygame.key.set_repeat(200, 300)
screen.fill(bg_color)

# Instantiations
level = Maze()
macgyver = MacGyver(level)

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

            # *In progress ---------------------------------------------------
            # print(level.items.get("neddle"))

            if (macgyver.x, macgyver.y) == (level.guard_pos):
                print("You win !!!")

            if (macgyver.case_x, macgyver.case_y) == (level.items.get("neddle")):
                print(".: Caught the neddle :.")

            if (macgyver.case_x, macgyver.case_y) == (level.items.get("ether")):
                print(".: Caught the ether :.")

            if (macgyver.case_x, macgyver.case_y) == (level.items.get("tube")):
                print(".: Caught the tube :.")

        level.display_maze(screen)
        screen.blit(macgyver.img_mac, (macgyver.x, macgyver.y))
        pygame.display.flip()
        clock.tick(30)  # 30 fps

pygame.quit()
