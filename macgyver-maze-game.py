#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" Mac Gyver Maze Game
Game in which we must move Mac Gyver to escape a labyrinth.
"""

import pygame

from classes import Maze, MacGyver
from constants import DISPLAY_SIZE, ICON_GAME, TITLE_WINDOW, IMG_MAC

pygame.init()

# variables
icon = pygame.image.load(ICON_GAME)
screen = pygame.display.set_mode(DISPLAY_SIZE)
bg_color = (173, 159, 146)
clock = pygame.time.Clock()

pygame.display.set_caption(TITLE_WINDOW)
pygame.display.set_icon(icon)
pygame.key.set_repeat(200, 300)
screen.fill(bg_color)

labyrinth = Maze()
macgyver = MacGyver(labyrinth)

game_continue = True

while game_continue:

    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and \
                event.key == pygame.K_ESCAPE:
            game_continue = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                macgyver.move("right")
            elif event.key == pygame.K_LEFT:
                macgyver.move("left")
            if event.key == pygame.K_UP:
                macgyver.move("up")
            if event.key == pygame.K_DOWN:
                macgyver.move("down")

        labyrinth.display_maze(screen)
        screen.blit(macgyver.img_mac, (macgyver.x, macgyver.y))
        pygame.display.flip()

pygame.quit()
