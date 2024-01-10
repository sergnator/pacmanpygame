from filesefun import *
import sys
import pygame
from MapWriter import generate_level


def add_button_back(back_image=None):
    def actual(func):
        def new_func(screen: pygame.Surface, *args, back_image=back_image):

            if back_image is None:
                back_image = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
                pygame.draw.rect(back_image, (0, 0, 0), (0, 0, *screen.get_size()))
            elif back_image == 'screen':
                back_image = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
                back_image = screen.convert(back_image)
            font = pygame.font.Font(None, 30)
            string_render_button = font.render('back', 1, pygame.Color('blue'))
            rect_QUIT = string_render_button.get_rect()
            rect_QUIT.x = 20
            rect_QUIT.y = 20
            rect_QUIT.w += 10
            rect_QUIT.h += 20
            args_ = func(screen, *args)
            while True:
                for event in pygame.event.get():
                    command = check(event, args_)
                    if command == 'return':
                        return
                    if event.type == pygame.MOUSEBUTTONUP:
                        if (event.pos[0] in list(range(10, 10 + rect_QUIT.w)) and
                                event.pos[1] in range(10, 10 + rect_QUIT.h)):
                            screen.fill((0, 0, 0))
                            return
                screen.blit(back_image, back_image.get_rect())
                screen.blit(string_render_button, rect_QUIT)
                draw(args_)
                pygame.display.flip()

        return new_func

    return actual


def get_name(screen: pygame.Surface):
    intro = 'input text'
    enter = 'press enter'
    input_text = '><'
    size = screen.get_size()
    text_cords = size[0] // 2
    font = pygame.font.Font(None, 30)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    return input_text[1:-1]
                elif event.key == pygame.K_BACKSPACE:
                    if input_text != '><':
                        input_text = input_text[:-2] + '<'
                else:
                    input_text = input_text[:-1] + event.unicode + '<'
        screen.fill((0, 0, 0))
        string_ = font.render(input_text, 1, pygame.Color('blue'))
        rect = string_.get_rect()
        rect.x = text_cords - rect.w / 2
        rect.y = text_cords - rect.h
        screen.blit(string_, rect)
        string_ = font.render(intro, 1, pygame.Color('blue'))
        rect = string_.get_rect()
        rect.x = text_cords - rect.w / 2
        rect.y = size[1] / 3
        screen.blit(string_, rect)
        string_ = font.render(enter, 1, pygame.Color('blue'))
        rect = string_.get_rect()
        rect.x = text_cords - rect.w / 2
        rect.y = size[1] / 4 * 3
        screen.blit(string_, rect)

        pygame.display.flip()


def start_menu(screen: pygame.Surface, all_sprites):
    menu = ['start', 'score', 'quit']
    screen.fill((0, 0, 0))
    size = screen.get_size()
    text_x_cords = size[0] // 2
    font = pygame.font.Font(None, 30)
    current_text = 0

    while True:
        text_y_cords = size[1] // 4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    current_text += 1
                elif event.key == pygame.K_UP:
                    current_text -= 1 if current_text != 0 else 0
                elif event.key == pygame.K_RETURN:
                    if current_text % len(menu) == 1:
                        score_menu(screen)
                        screen.fill((0, 0, 0))
                    elif current_text % len(menu) == 2:
                        pygame.quit()
                        sys.exit()
                    elif current_text % len(menu) == 0:
                        change_map(screen, all_sprites)
                        return

        for word in menu:
            color = 'yellow' if menu.index(word) == current_text % len(menu) else 'blue'
            string_render = font.render(word, 1, pygame.Color(color))
            rect = string_render.get_rect()
            rect.x = text_x_cords - rect.w / 2
            rect.y = text_y_cords
            text_y_cords += 50
            screen.blit(string_render, rect)
            pygame.display.flip()


@add_button_back()
def score_menu(screen: pygame.Surface):
    users = get_users()
    users.sort(key=lambda x: int(x[Constants.record_time_key]))
    font = pygame.font.Font(None, 30)

    while len(users) < 3:
        users.append([' ', ' ', ' ', ' '])
    texts = [['RANK', 'SCORE', 'NAME'], ]
    for i in range(3):
        texts.append(
            [str(i + 1) if users[i][Constants.record_time_key] != ' ' else ' ', users[i][Constants.record_time_key],
             users[i][Constants.name_key]])
    color = (153, 255, 153)
    global draw
    global check

    def draw(args):
        texts = args[0]
        color = args[1]
        for i in range(len(texts)):
            y = 190 + 20 * i
            for j in range(len(texts[i])):
                x = 100 + 80 * j
                text_render = font.render(str(texts[i][j]), 1, color)
                rect = text_render.get_rect()
                rect.x = x
                rect.y = y
                screen.blit(text_render, rect)

    def check(event, args):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    return [texts, color]


@add_button_back()
def change_map(screen: pygame.Surface, all_sprites):
    maps = get_maps()
    font = pygame.font.Font(None, 30)
    size = screen.get_size()
    current_map = 0
    global draw
    global check

    def draw(args):
        for i in range(len(maps)):
            current_map = args[0]
            color = 'blue' if current_map % len(maps) != i else 'yellow'
            string_render = font.render(str(maps[i]), 1, pygame.Color(color))
            rect = string_render.get_rect()
            rect.x = size[0] // 2 - rect.w // 2
            rect.y = 100 + 30 * i
            screen.blit(string_render, rect)

    def check(event, args):
        all_sprites = args[1]
        current_map = args[0]
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                current_map += 1
            elif event.key == pygame.K_UP:
                current_map -= 1 if current_map != 0 else 0
            elif event.key == pygame.K_RETURN:
                generate_level(maps[current_map % len(maps)] + ".txt", all_sprites)
                return 'return'
        args[0] = current_map

    return [current_map, all_sprites]


