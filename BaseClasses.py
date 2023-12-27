import os
import sys
import pygame


# исключения
class BasePacmanExceptionsGroup(Exception):
    pass


class NameTaken(BasePacmanExceptionsGroup):
    pass


# константы
class Constants:
    DataBaseOfScore = 'data/databases/score.sqlite'
    Maps = 'data/maps/'
    WinResult = 1
    LoseResult = 0
    Images = 'data/images/'
    id_key = 0
    name_key = 1
    record_time_key = 2
    record_map_key = 3
    Music = 'data/music/'


class HelpFunctions:
    @staticmethod
    def load_image(name, colorkey=None):
        fullname = Constants.Images + name
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)

        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image
