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

    def load_level(filename):
        filename = "data/" + filename
        # читаем уровень, убирая символы перевода строки
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]

        # и подсчитываем максимальную длину
        max_width = max(map(len, level_map))

        # дополняем каждую строку пустыми клетками ('.')
        return list(map(lambda x: x.ljust(max_width, '.'), level_map))

