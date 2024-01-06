from pacmansprite import *


class Ghost(AnimatedSprite):

    def __init__(self, x, y, group):
        surface = HelpFunctions.load_image("red_ghost.png")
        super().__init__(HelpFunctions.load_image((pygame.transform.scale(surface, (50, 60)), 2, 1, x, y, group))
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