import pygame
from start_menu import *



pygame.init()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((500, 500))

name = get_name(screen)

start_menu(screen, all_sprites)