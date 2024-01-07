import pygame
from BaseClasses import HelpFunctions


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, group):
        super().__init__(group)
        self.image = pygame.Surface((w, h), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, pygame.Color('blue'), (0, 0, w, h))
        self.rect = pygame.Rect(x, y, w, h)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, group):
        super().__init__(group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

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
        self.vx = -10
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

    def __init__(self, x, y, group):
        surface = HelpFunctions.load_image("red_ghost.png")
        super().__init__(pygame.transform.scale(surface, (128,  64)), 2, 1, x, y, group)
        self.vx = -7
        self.vy = 0
        self.group = group

    def update(self):
        super().update()
        self.rect = self.rect.move(self.vx, self.vy)
        if self.vx < 0:
            self.image = pygame.transform.flip(self.frames[self.cur_frame], True, False)
        elif self.vx > 0:
            self.image = self.frames[self.cur_frame]
