from pacmansprites import *
from BaseClasses import PacmanNotStated


def load_level(filename):
    filename = "data/maps/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    return level_map


def generate_level(level, all_sprites):
    level = load_level(level)
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '#':
                Wall(x, y, all_sprites)
            elif level[y][x] == '@':
                new_player = Pacman(x, y, all_sprites)
            elif level[y][x] == 'R':
                red_ghost = Ghost('red_ghost', x, y, all_sprites)
            elif level[y][x] == 'B':
                blue_ghost = Ghost('blue_ghost', x, y, all_sprites)
            elif level[y][x] == 'P':
                pink_ghost = Ghost('pink_ghost', x, y, all_sprites)
            elif level[y][x] == 'O':
                orange_ghost = Ghost('orange_ghost', x, y, all_sprites)
            elif level[y][x] == ' ':
                Coin(x, y, [all_sprites])
            elif level[y][x] == ':':
                Wall(x, y, all_sprites, color='red')
            elif level[y][x] == ';':
                Wall(x, y, all_sprites, color='black')
    if new_player is None:
        raise PacmanNotStated
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y
