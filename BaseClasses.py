import os

import pygame
import Constants


# исключения
class BasePacmanExceptionsGroup(Exception):
    pass


class NameNotTaken(BasePacmanExceptionsGroup):
    pass


class NotFoundFile(BasePacmanExceptionsGroup):
    pass


class PacmanNotStated(BasePacmanExceptionsGroup):
    pass


class HelpFunctions:
    @staticmethod
    def load_image(name, colorkey=None):
        fullname = Constants.Images + name
        if not os.path.isfile(fullname):
            NotFoundFile('файл с названием: ' + name + ' не найден')
        image = pygame.image.load(fullname)

        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image
