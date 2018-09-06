from random import choice

import pygame

from constants import (IMG_ETHER, IMG_GUARDIAN, IMG_MAC, IMG_NEDDLE,
                       IMG_SPRITES, IMG_TUBE, SPRITE_NUMBER)


class Maze:
    """ Open the text file and generates the structure of the labyrinth :
            Maze("filename.txt")
        By default, open the original file "labyrinth-scheme.txt"
    """

    def __init__(self, txt_file="labyrinth_scheme.txt"):
        self.txt_file = txt_file
        self.maze_structure = []
        self.__reader_file()
        self.__place_random_objects()

    def __reader_file(self):
        """ Method for generating the level based on the file.
        We create a general list, containing a list by line to display.
        """
        try:
            with open(self.txt_file, "r") as f:

                lines = f.readlines()[9:]

                for line in lines:
                    level_line = []
                    # We go through the sprites (letters) contained in the file.
                    for sprite in line.strip("\n"):
                        # We add the sprite to the list of the line
                        level_line.append(sprite)
                    # Add the line to the level list
                    self.maze_structure.append(level_line)
                # We safeguard this structure
                return self.maze_structure

        except FileNotFoundError:
            print("File not found or incorrect !!!")

    def __get_floor(self):
        line_number = 0
        floor_pos = []

        for line in self.maze_structure:
            line_number += 1
            for i, sprite in enumerate(line):
                if sprite == " ":
                    floor_pos.append([line_number - 1, i])
        return floor_pos

    def __place_random_objects(self):
        objects = ["neddle", "tube", "ether"]
        floor = self.__get_floor()

        for i in range(0, len(objects)):
            line_number, index = choice(floor)
            self.maze_structure[line_number].pop(index)
            self.maze_structure[line_number].insert(index, objects[i])
        return self.maze_structure

    def display_maze(self, window):
        """ In the text file, the characters correspond to:
                > " " = floor
                > "w" = wall
                > "s" = macgyver (start)
                > "e" = guardian (end)
        """
        img_wall = pygame.image.load(IMG_SPRITES).convert()
        wall = pygame.transform.scale(
            img_wall.subsurface(300, 0, 20, 20), (30, 30))

        img_floor = pygame.image.load(IMG_SPRITES).convert()
        floor = pygame.transform.scale(
            img_floor.subsurface(160, 40, 20, 20), (30, 30))

        # img_macgyver = pygame.image.load(IMG_MAC).convert_alpha()
        # macgyver = pygame.transform.scale(img_macgyver, (30, 30))

        img_guardian = pygame.image.load(IMG_GUARDIAN).convert_alpha()
        guardian = pygame.transform.scale(img_guardian, (30, 30))

        img_neddle = pygame.image.load(IMG_NEDDLE).convert_alpha()
        neddle = pygame.transform.scale(img_neddle, (30, 30))

        img_tube = pygame.image.load(IMG_TUBE).convert_alpha()
        tube = pygame.transform.scale(img_tube, (30, 30))

        img_ether = pygame.image.load(IMG_ETHER).convert_alpha()
        ether = pygame.transform.scale(img_ether, (30, 30))

        line_number = 0
        for line in self.maze_structure:
            case_number = 0
            for sprite in line:
                pos_x = case_number * 30
                pos_y = line_number * 30
                if sprite == " ":
                    window.blit(floor, (pos_x, pos_y))
                elif sprite == "w":
                    window.blit(wall, (pos_x, pos_y))
                # elif sprite == "s":
                #     window.blit(macgyver, (pos_x, pos_y))
                elif sprite == "e":
                    window.blit(guardian, (pos_x, pos_y))
                elif sprite == "neddle":
                    window.blit(neddle, (pos_x, pos_y))
                elif sprite == "tube":
                    window.blit(tube, (pos_x, pos_y))
                elif sprite == "ether":
                    window.blit(ether, (pos_x, pos_y))
                case_number += 1
            line_number += 1


class MacGyver:
    def __init__(self, labyrinth):
        self.labyrinth = labyrinth
        img_macgyver = pygame.image.load(IMG_MAC).convert_alpha()
        self.img_mac = pygame.transform.scale(img_macgyver, (30, 30))
        # Initial position
        self.case_x = 1
        self.case_y = 1
        self.x = 1 * 30
        self.y = 1 * 30

    def move(self, direction):
        # Move to right
        if direction == "right":
            if self.labyrinth.maze_structure[self.case_y][self.case_x+1] != "w":
                self.case_x += 1
                self.x = self.case_x * 30

        # Move to left
        if direction == "left":
            if self.labyrinth.maze_structure[self.case_y][self.case_x-1] != "w":
                self.case_x -= 1
                self.x = self.case_x * 30

        # Move to up
        if direction == "up":
            if self.labyrinth.maze_structure[self.case_y-1][self.case_x] != "w":
                self.case_y -= 1
                self.y = self.case_y * 30

        # Move to down
        if direction == "down":
            if self.labyrinth.maze_structure[self.case_y+1][self.case_x] != "w":
                self.case_y += 1
                self.y = self.case_y * 30


def main():
    labyrinth = Maze()
    print("Maze 15x15 with random objects:\n===============================")
    for line in labyrinth.maze_structure:
        print(line)


if __name__ == '__main__':
    main()
