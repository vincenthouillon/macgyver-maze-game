from random import randrange

import pygame

from includes.constants import (FILE_TEXT, IMG_ETHER, IMG_GUARDIAN, IMG_MAC,
                                IMG_NEDDLE, IMG_SPRITES, IMG_TUBE, OBJECTS,
                                SPRITE_NUMBER, SPRITE_SIZE)


class Maze:
    """Open the text file and generates the structure of the labyrinth:

    Arguments:
        file {path} -- Text path file

    By default, open the original file 'includes/labyrinth-scheme.txt.'
    """

    def __init__(self, txt_file=FILE_TEXT):
        self.txt_file = txt_file
        self.structure = 0
        self.macgyver_pos = ()
        self.floor = 0

        # Launch private mehtod
        self.__generate()
        self.__get_position_mac()

    def __generate(self):
        """Private method to generate the file-based labyrinth and to 
        randomly place objects there.
        """
        # Read the text file and generate the labyrinth
        try:
            with open(self.txt_file, "r") as f:
                # Read the file from line 12 to 26
                lines = f.readlines()[11:26]
                maze_structure = []
                maze_floor = []
                for line in lines:
                    level_line = []
                    # We go through the sprites (letters) contained in the file
                    for sprite in line.strip("\n"):
                        # We add the sprite to the list of the line
                        level_line.append(sprite)
                    # Add the line to the level list
                    maze_structure.append(level_line)

        except FileNotFoundError:
            print("File not found or incorrect !!!")

        self.structure = maze_structure
        self.random_objects()

    def random_objects(self):
        """ Place the objects randomly. """
        loot = 0
        while loot < len(OBJECTS):
            x_object = randrange(0, SPRITE_NUMBER)
            y_object = randrange(0, SPRITE_NUMBER)

            if self.structure[y_object][x_object] == " ":
                self.structure[y_object][x_object] = OBJECTS[loot]
                loot += 1

    def __get_position_mac(self):
        """Private method for get the macgyver position."""
        line_number = 0
        for line in self.structure:
            case_number = 0
            for sprite in line:
                pos_x = case_number
                pos_y = line_number
                if sprite == "s":
                    self.macgyver_pos = (pos_x, pos_y)
                case_number += 1
            line_number += 1

    def display_maze(self, window):
        """Initialize a window or screen for display in pygame.

        Arguments:
            window {object} -- window = pygame.display.set_mode(x, y)
        """
        DIM_SPRITE = (SPRITE_SIZE, SPRITE_SIZE)

        img_wall = pygame.image.load(IMG_SPRITES).convert()
        wall = pygame.transform.scale(
            img_wall.subsurface(300, 0, 20, 20), (DIM_SPRITE))

        img_floor = pygame.image.load(IMG_SPRITES).convert()
        floor = pygame.transform.scale(
            img_floor.subsurface(160, 40, 20, 20), (DIM_SPRITE))

        img_guardian = pygame.image.load(IMG_GUARDIAN).convert_alpha()
        guardian = pygame.transform.scale(img_guardian, (DIM_SPRITE))

        img_neddle = pygame.image.load(IMG_NEDDLE).convert_alpha()
        neddle = pygame.transform.scale(img_neddle, (DIM_SPRITE))

        img_tube = pygame.image.load(IMG_TUBE).convert_alpha()
        tube = pygame.transform.scale(img_tube, (DIM_SPRITE))

        img_ether = pygame.image.load(IMG_ETHER).convert_alpha()
        ether = pygame.transform.scale(img_ether, (DIM_SPRITE))

        line_number = 0
        for line in self.structure:
            case_number = 0
            for sprite in line:
                pos_x = case_number * SPRITE_SIZE
                pos_y = line_number * SPRITE_SIZE
                if sprite == " " or sprite == "s":
                    window.blit(floor, (pos_x, pos_y))
                elif sprite == "w":
                    window.blit(wall, (pos_x, pos_y))
                elif sprite == "g":
                    window.blit(guardian, (pos_x, pos_y))
                elif sprite == "e":
                    window.blit(floor, (pos_x, pos_y))
                elif sprite == "neddle":
                    window.blit(neddle, (pos_x, pos_y))
                elif sprite == "tube":
                    window.blit(tube, (pos_x, pos_y))
                elif sprite == "ether":
                    window.blit(ether, (pos_x, pos_y))
                case_number += 1
            line_number += 1
