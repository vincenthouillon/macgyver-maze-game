""" Mac Gyver Maze Game
Game in which we must move Mac Gyver to escape a labyrinth.
"""

import pygame

from classes import Level
from constants import DISPLAY_SIZE, ICON_GAME, TITLE_WINDOW

pygame.init()

# variables
icon = pygame.image.load(ICON_GAME)
screen = pygame.display.set_mode(DISPLAY_SIZE)
clock = pygame.time.Clock()

pygame.display.set_caption(TITLE_WINDOW)
pygame.display.set_icon(icon)


game_continue = True

while game_continue:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and \
                event.key == pygame.K_ESCAPE:
            game_continue = False

    level = Level('lvl_01.json')
    level.reader_file()
    level.display_maze(screen)

    pygame.display.update()
    clock.tick(30)


pygame.quit()
