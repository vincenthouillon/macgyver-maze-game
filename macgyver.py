import pygame

from constants import IMG_MAC, SPRITE_NUMBER, SPRITE_SIZE


class MacGyver:
    """ Character management. """

    def __init__(self, level):
        self.level = level
        self.guard_pos = ()
        self.macgyver_pos = ()
        self.img_mac = pygame.transform.scale(
            pygame.image.load(IMG_MAC).convert_alpha(), (SPRITE_SIZE, SPRITE_SIZE))

        # *Initial position of MacGyver
        self.case_x, self.case_y = level.macgyver_pos
        self.x = self.case_x * SPRITE_SIZE
        self.y = self.case_y * SPRITE_SIZE
        print(f"Position de mac : {level.macgyver_pos}")  # !debug
        print(f"Position du gardien : {level.guard_pos}")  # !debug

    def move(self, direction):
        """ Move the character if there is no wall.

        Arguments:
            direction {text} -- 'right', 'left', 'up', 'down'

        """

        if direction == "right":
            if self.case_x < SPRITE_NUMBER -1:
                if self.level.structure[self.case_y][self.case_x + 1] != "w":
                    self.case_x += 1
                    self.x = self.case_x * SPRITE_SIZE
                    print(f"RIGHT: case_x = {self.case_x}, x = {self.x}")  # !debug

        if direction == "left":
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != "w":
                    self.case_x -= 1
                    self.x = self.case_x * SPRITE_SIZE
                    print(f"LEFT: case_x = {self.case_x}, x = {self.x}")  # !debug

        if direction == "up":
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != "w":
                    self.case_y -= 1
                    self.y = self.case_y * SPRITE_SIZE
                    print(f"UP: case_y = {self.case_y}, y = {self.y}")  # !debug

        if direction == "down":
            if self.case_y < SPRITE_NUMBER -1:
                if self.level.structure[self.case_y + 1][self.case_x] != "w":
                    self.case_y += 1
                    self.y = self.case_y * SPRITE_SIZE
                    print(f"DOWN: case_y = {self.case_y}, y = {self.y}")  # !debug
