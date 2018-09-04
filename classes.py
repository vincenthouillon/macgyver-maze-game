import json

import pygame

from constants import IMG_GUARDIAN, IMG_MAC, IMG_SPRITES


class Level:
    """ Docstrings
    """
    # TODO : Ajouter la fonction "Objects" et "character"

    def __init__(self, level_file):
        self.file = level_file
        self.structure = 0

    def reader_file(self):
        """ Method for generating the level based on the file.
        We create a general list, containing a list by line to display.
        """

        with open(self.file, "r") as f:
            self.structure = json.load(f)
            return self.structure

    def display_maze(self, window):
        """ In the json file, the numbers correspond to:
                > 0 = floor
                > 1 = wall
                > 2 = start
                > 3 = end
        """
        img_wall = pygame.image.load(IMG_SPRITES).convert()
        wall = pygame.transform.scale(
            img_wall.subsurface(300, 0, 20, 20), (30, 30))
        img_floor = pygame.image.load(IMG_SPRITES).convert()
        floor = pygame.transform.scale(
            img_floor.subsurface(160, 40, 20, 20), (30, 30))
        img_start = pygame.image.load(IMG_MAC).convert_alpha()
        start = pygame.transform.scale(img_start, (30, 30))
        # start = pygame.transform.scale(
        #     img_start.subsurface(160, 20, 20, 20), (30, 30))
        img_end = pygame.image.load(IMG_GUARDIAN).convert_alpha()
        end = pygame.transform.scale(img_end, (30, 30))

        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                x = num_case * 30
                y = num_line * 30
                if sprite == 0:
                    window.blit(floor, (x, y))
                elif sprite == 1:
                    window.blit(wall, (x, y))
                elif sprite == 2:
                    window.blit(start, (x, y))
                elif sprite == 3:
                    window.blit(end, (x, y))
                num_case += 1
            num_line += 1


def main():
    level = Level("lvl_01.json")
    print(level.reader_file())  # For debugg


if __name__ == '__main__':
    main()
