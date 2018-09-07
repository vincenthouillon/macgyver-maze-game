from random import choice

import pygame

from constants import (IMG_ETHER, IMG_GUARDIAN, IMG_MAC, IMG_NEDDLE,
                       IMG_SPRITES, IMG_TUBE, SPRITE_NUMBER, SPRITE_SIZE)


class Maze:
    """ Open the text file and generates the structure of the labyrinth :

            Maze(file)

        By default, open the original file "labyrinth-scheme.txt"
    """

    def __init__(self, txt_file="labyrinth_scheme.txt"):
        self.txt_file = txt_file
        self.maze = []
        self.items = {}
        self.macgyver_pos = ()
        self.guard_pos = ()
        self.__generate()
        self.__place_random_objects()

    def __generate(self):
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
                    self.maze.append(level_line)
                # We safeguard this structure
                return self.maze

        except FileNotFoundError:
            print("File not found or incorrect !!!")

    def __get_position(self):
        pos_y = 0
        floor_pos = []
    
        for line in self.maze:
            pos_y += 1
            for x, sprite in enumerate(line):
                if sprite == "s":
                    self.macgyver_pos = (x, pos_y -1)
                if sprite == "e":
                    self.guard_pos = (x * SPRITE_SIZE, (pos_y -1) * SPRITE_SIZE)
                if sprite == " ":
                    floor_pos.append([pos_y - 1, x])
        return floor_pos
        

    def __place_random_objects(self):
        objects = ["neddle", "tube", "ether"]
        floor = self.__get_position()

        for i in range(0, len(objects)):
            pos_y, pos_x = choice(floor)
            self.maze[pos_y].pop(pos_x)
            self.maze[pos_y].insert(pos_x, objects[i])
            self.__get_position()
            
            # add in dictionnary 'self.items'
            self.items[objects[i]] = (pos_x, pos_y)
            # print(objects[i], pos_y, pos_x)  # !debug
            
        print(self.items)
        return self.maze

    def display_maze(self, window):
        """For display a game.

            Keyword arguments:
            window -- X = pygame.display.set_mode(x, y)
        """
        
        DIM_SPRITE = (SPRITE_SIZE, SPRITE_SIZE)

        img_wall = pygame.image.load(IMG_SPRITES).convert_alpha()
        wall = pygame.transform.scale(
            img_wall.subsurface(300, 0, 20, 20), (DIM_SPRITE))

        img_floor = pygame.image.load(IMG_SPRITES).convert_alpha()
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
        for line in self.maze:
            case_number = 0
            for sprite in line:
                pos_x = case_number * SPRITE_SIZE
                pos_y = line_number * SPRITE_SIZE
                if sprite == " ":
                    window.blit(floor, (pos_x, pos_y))
                elif sprite == "w":
                    window.blit(wall, (pos_x, pos_y))
                elif sprite == "s":  # *starting position but displaying floor
                    window.blit(floor, (pos_x, pos_y))
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


def main():
    labyrinth = Maze()
    print("Maze 15x15 with random objects:\n===============================")
    for line in labyrinth.maze:
        print(line)

if __name__ == '__main__':
    main()
