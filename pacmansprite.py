import pygame
from BaseClasses import HelpFunctions
from Constants import CellWidth, CellHeight


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = pygame.Surface((CellWidth, CellHeight), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, pygame.Color('blue'), (0, 0, CellWidth, CellHeight))
        self.rect = pygame.Rect(x * CellWidth, y * CellHeight, CellWidth, CellHeight)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, group, is_gost=False):
        super().__init__(group)
        self.frames = []
        if is_gost:
            self.cut_sheet(pygame.transform.scale(sheet, (CellWidth * columns * 2, CellHeight * rows * 2)), columns,
                           rows)
        else:
            self.cut_sheet(pygame.transform.scale(sheet, (CellWidth * columns, CellHeight * rows)), columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        if is_gost:
            self.rect = self.rect.move(x * CellWidth - 10, y * CellHeight / 2 - 10)
        else:
            self.rect = self.rect.move(x * CellWidth, y * CellHeight)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Pacman(AnimatedSprite):

    def __init__(self, x, y, group):
        super().__init__(HelpFunctions.load_image('pacman.png'), 4, 1, x, y, group)
        self.vx = 0
        self.vy = 0
        self.group = group

    def update(self):
        super().update()
        self.rect = self.rect.move(self.vx, self.vy)
        if self.vx < 0:
            self.image = pygame.transform.flip(self.frames[self.cur_frame], True, False)
        elif self.vx > 0:
            self.image = self.frames[self.cur_frame]
        elif self.vy < 0:
            self.image = pygame.transform.rotate(self.frames[self.cur_frame], 90)
        elif self.vy > 0:
            self.image = pygame.transform.rotate(self.frames[self.cur_frame], -90)


class Ghost(AnimatedSprite):

    def __init__(self, name, x, y, group):
        surface = HelpFunctions.load_image(f"{name}.png")
        super().__init__(surface, 2, 1, x, y, group, is_gost=True)
        self.vx = 0
        self.vy = 0
        self.group = group

    def update(self):
        super().update()
        self.rect = self.rect.move(self.vx, self.vy)
        if self.vx < 0:
            self.image = pygame.transform.flip(self.frames[self.cur_frame], True, False)

        elif self.vx >= 0:
            self.image = self.frames[self.cur_frame]
