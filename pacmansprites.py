import pygame
from random import randint
from BaseClasses import HelpFunctions
from Constants import CellWidth, CellHeight


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = pygame.Surface((CellWidth, CellHeight), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, pygame.Color('blue'), (0, 0, CellWidth - 10, CellHeight - 10))
        self.rect = pygame.Rect(x * CellWidth + 5, y * CellHeight + 5, CellWidth, CellHeight)


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
            self.rect = self.rect.move(x * CellWidth - 10, y * CellHeight - 10)
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
    c = 0

    def __init__(self, x, y, group):
        super().__init__(HelpFunctions.load_image('pacman.png'), 4, 1, x, y, group)
        self.vx = 0
        self.vy = 0
        self.group = group

    def update(self):
        if self.c % 3 == 0:
            super().update()

        if self.vx < 0:
            self.image = pygame.transform.flip(self.frames[self.cur_frame], True, False)
            if self.c % 5 == 0:
                for sprite in self.groups()[0].sprites():
                    if sprite.rect.x + CellWidth - 5 == self.rect.x and sprite.rect.y - 5 == self.rect.y:
                        self.c += 1
                        return
                self.rect = self.rect.move(-CellWidth, 0)
        elif self.vx > 0:
            self.image = self.frames[self.cur_frame]
            if self.c % 5 == 0:
                for sprite in self.groups()[0].sprites():
                    if sprite.rect.x - CellWidth - 5 == self.rect.x and sprite.rect.y - 5 == self.rect.y:
                        self.c += 1
                        return
                self.rect = self.rect.move(CellWidth, 0)
        elif self.vy < 0:
            self.image = pygame.transform.rotate(self.frames[self.cur_frame], 90)
            if self.c % 5 == 0:
                for sprite in self.groups()[0].sprites():
                    if sprite.rect.y + CellHeight - 5 == self.rect.y and sprite.rect.x - 5 == self.rect.x:
                        self.c += 1
                        return
                self.rect = self.rect.move(0, -CellHeight)
        elif self.vy > 0:
            self.image = pygame.transform.rotate(self.frames[self.cur_frame], -90)
            if self.c % 5 == 0:
                for sprite in self.groups()[0].sprites():
                    if sprite.rect.y - CellHeight - 5 == self.rect.y and sprite.rect.x - 5 == self.rect.x:
                        self.c += 1
                        return
                self.rect = self.rect.move(0, CellHeight)
        self.c += 1


class Ghost(AnimatedSprite):
    c = 0

    def __init__(self, name, x, y, group):
        surface = HelpFunctions.load_image(f"{name}.png")
        super().__init__(surface, 2, 1, x, y, group, is_gost=True)
        a = randint(1, 4)
        if a == 1:
            self.vx = 1
            self.vy = 0
        if a == 2:
            self.vx = -1
            self.vy = 0
        if a == 3:
            self.vx = 0
            self.vy = 1
        if a == 4:
            self.vx = 0
            self.vy = -1
        self.group = group

    def update(self):
        if self.c % 3 == 0:
            super().update()

        if self.vx < 0:
            self.image = pygame.transform.flip(self.frames[self.cur_frame], True, False)
            if self.c % 5 == 0:
                for sprite in self.groups()[0].sprites():
                    if sprite.rect.x + CellWidth - 5 == self.rect.x + 10 and sprite.rect.y - 5 == self.rect.y + 10:
                        self.c += 1
                        a = randint(1, 3)
                        if a == 1:
                            self.vx = 0
                            self.vy = 1
                        if a == 2:
                            self.vx = 0
                            self.vy = -1
                        if a == 3:
                            self.vx = 1
                            self.vy = 0
                        return
                self.rect = self.rect.move(-CellWidth, 0)
        elif self.vx > 0:
            self.image = self.frames[self.cur_frame]
            if self.c % 5 == 0:
                for sprite in self.groups()[0].sprites():
                    if sprite.rect.x - CellWidth - 5 == self.rect.x + 10 and sprite.rect.y - 5 == self.rect.y + 10:
                        self.c += 1
                        a = randint(1, 3)
                        if a == 1:
                            self.vx = 0
                            self.vy = 1
                        if a == 2:
                            self.vx = 0
                            self.vy = -1
                        if a == 3:
                            self.vx = -1
                            self.vy = 0
                        return
                self.rect = self.rect.move(CellWidth, 0)
        elif self.vy < 0:
            if self.c % 5 == 0:
                for sprite in self.groups()[0].sprites():
                    if sprite.rect.y + CellHeight - 5 == self.rect.y + 10 and sprite.rect.x - 5 == self.rect.x + 10:
                        print(1)
                        self.c += 1
                        a = randint(1, 3)
                        if a == 1:
                            self.vx = 0
                            self.vy = 1
                        if a == 2:
                            self.vx = -1
                            self.vy = 0
                        if a == 3:
                            self.vx = 1
                            self.vy = 0
                        return
                self.rect = self.rect.move(0, -CellHeight)
        elif self.vy > 0:
            if self.c % 5 == 0:
                for sprite in self.groups()[0].sprites():
                    if sprite.rect.y - CellHeight - 5 == self.rect.y + 10 and sprite.rect.x - 5 == self.rect.x + 10:
                        self.c += 1
                        a = randint(1, 3)
                        if a == 1:
                            self.vx = 1
                            self.vy = 0
                        if a == 2:
                            self.vx = -1
                            self.vy = 0
                        if a == 3:
                            self.vx = 0
                            self.vy = -1
                        return
                self.rect = self.rect.move(0, CellHeight)
        self.c += 1


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        super().__init__(*group)
        self.image = pygame.surface.Surface((CellWidth, CellHeight), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color('orange'), (0.5 * CellWidth, 0.5 * CellHeight), 2)
        self.rect = self.image.get_rect()
        self.rect.x = CellWidth * x
        self.rect.y = CellHeight * y

