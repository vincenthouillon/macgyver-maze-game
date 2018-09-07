import pygame

from constants import IMG_MAC, SPRITE_NUMBER, SPRITE_SIZE


class MacGyver:
    def __init__(self, labyrinth):
        self.labyrinth = labyrinth
        self.guard_pos = ()
        self.macgyver_pos = ()
        self.img_mac = pygame.transform.scale(
            pygame.image.load(IMG_MAC).convert_alpha(), (SPRITE_SIZE, SPRITE_SIZE))

        # * Initial position
        self.case_x, self.case_y = labyrinth.macgyver_pos
        self.x = self.case_x * SPRITE_SIZE
        self.y = self.case_y * SPRITE_SIZE
        print(f"Position de mac : {labyrinth.macgyver_pos}")  # !debug
        print(f"Position du gardien : {labyrinth.guard_pos}")  # !debug


    def move(self, direction):
        # Move to right
        if direction == "right":
            if self.labyrinth.maze[self.case_y][self.case_x + 1] != "w":
                self.case_x += 1
                self.x = self.case_x * SPRITE_SIZE
                print(f"RIGHT: case_x = {self.case_x}, x = {self.x}")  # !debug

        # Move to left
        if direction == "left":
            if self.labyrinth.maze[self.case_y][self.case_x - 1] != "w":
                self.case_x -= 1
                self.x = self.case_x * SPRITE_SIZE
                print(f"LEFT: case_x = {self.case_x}, x = {self.x}")  # !debug

        # Move to up
        if direction == "up":
            if self.labyrinth.maze[self.case_y - 1][self.case_x] != "w":
                self.case_y -= 1
                self.y = self.case_y * SPRITE_SIZE
                print(f"UP: case_y = {self.case_y}, y = {self.y}")  # !debug

        # Move to down
        if direction == "down":
            if self.labyrinth.maze[self.case_y + 1][self.case_x] != "w":
                self.case_y += 1
                self.y = self.case_y * SPRITE_SIZE
                print(f"DOWN: case_y = {self.case_y}, y = {self.y}")  # !debug
