import json
from random import choice

import pygame

from constants import (IMG_ETHER, IMG_GUARDIAN, IMG_MAC, IMG_NEDDLE,
                       IMG_SPRITES, IMG_TUBE)


class Level:
    """ Docstrings
    """
    # TODO : Ajouter la fonction "Objects" et "character"

    def __init__(self, level_file):
        self.file = level_file
        self.structure = 0
        self.maze = []
        self.__reader_file()
        self.__place_random_objects()

    def __reader_file(self):
        """ Method for generating the level based on the file.
        We create a general list, containing a list by line to display.
        """

        try:
            with open(self.file, "r") as f:
                self.structure = json.load(f)
                return self.structure
        except FileNotFoundError:
            print("File not found")

    def __get_floor(self):
        line_number = 0
        floor_pos = []

        for line in self.structure:
            line_number += 1
            for i, sprite in enumerate(line):
                if sprite == 0:
                    floor_pos.append([line_number - 1, i])
        return floor_pos

    def __place_random_objects(self):
        objects = ["neddle", "tube", "ether"]
        floor = self.__get_floor()
        intial_maze = self.__reader_file()

        for i in range(0, len(objects)):
            line_number, index = choice(floor)
            intial_maze[line_number].pop(index)
            intial_maze[line_number].insert(index, objects[i])
        self.maze = intial_maze
        return self.maze

    def display_maze(self, window):
        """ In the json file, the numbers correspond to:
                > 0 = floor
                > 1 = wall
                > 2 = macgyver (start)
                > 3 = guardian (end)
        """
        img_wall = pygame.image.load(IMG_SPRITES).convert()
        wall = pygame.transform.scale(
            img_wall.subsurface(300, 0, 20, 20), (30, 30))

        img_floor = pygame.image.load(IMG_SPRITES).convert()
        floor = pygame.transform.scale(
            img_floor.subsurface(160, 40, 20, 20), (30, 30))

        img_macgyver = pygame.image.load(IMG_MAC).convert_alpha()
        macgyver = pygame.transform.scale(img_macgyver, (30, 30))

        img_guardian = pygame.image.load(IMG_GUARDIAN).convert_alpha()
        guardian = pygame.transform.scale(img_guardian, (30, 30))

        img_neddle = pygame.image.load(IMG_NEDDLE).convert_alpha()
        neddle = pygame.transform.scale(img_neddle, (30, 30))
        
        img_tube = pygame.image.load(IMG_TUBE).convert_alpha()
        tube = pygame.transform.scale(img_tube, (30, 30))
        
        img_ether = pygame.image.load(IMG_ETHER).convert_alpha()
        ether = pygame.transform.scale(img_ether, (30, 30))

        num_line = 0
        for line in self.maze:
            num_case = 0
            for sprite in line:
                x = num_case * 30
                y = num_line * 30
                if sprite == 0:
                    window.blit(floor, (x, y))
                elif sprite == 1:
                    window.blit(wall, (x, y))
                elif sprite == 2:
                    window.blit(macgyver, (x, y))
                elif sprite == 3:
                    window.blit(guardian, (x, y))
                elif sprite == "neddle":
                    window.blit(neddle, (x, y))
                elif sprite == "tube":
                    window.blit(tube, (x, y))
                elif sprite == "ether":
                    window.blit(ether, (x, y))
                num_case += 1
            num_line += 1


def main():
    level = Level("lvl_01.json")
    print(level.maze)  # for debug


if __name__ == '__main__':
    main()
