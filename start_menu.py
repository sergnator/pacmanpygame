import sys

from BaseClasses import *
import pygame


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
