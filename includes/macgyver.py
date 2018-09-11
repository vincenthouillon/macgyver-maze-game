import pygame

from includes.constants import IMG_MAC, SPRITE_NUMBER, SPRITE_SIZE


class MacGyver:
    """MacGyver movement management."""

    def __init__(self, level):
        self.level = level

        # Initial position of MacGyver
        self.case_x, self.case_y = level.macgyver_pos
        self.x = self.case_x * SPRITE_SIZE
        self.y = self.case_y * SPRITE_SIZE

    def move(self, direction):
        """Move the character if there is no wall or if it does not 
        overflow the labyrinth.

        Arguments:
            direction {'str'} -- 'right', 'left', 'up', 'down'
        """
        if direction == "right":
            if self.case_x < SPRITE_NUMBER - 1:
                if self.level.structure[self.case_y][self.case_x + 1] != "w":
                    self.case_x += 1
                    self.x = self.case_x * SPRITE_SIZE

        if direction == "left":
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != "w":
                    self.case_x -= 1
                    self.x = self.case_x * SPRITE_SIZE

        if direction == "up":
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != "w":
                    self.case_y -= 1
                    self.y = self.case_y * SPRITE_SIZE

        if direction == "down":
            if self.case_y < SPRITE_NUMBER - 1:
                if self.level.structure[self.case_y + 1][self.case_x] != "w":
                    self.case_y += 1
                    self.y = self.case_y * SPRITE_SIZE
