import pygame
from start_menu import *



pygame.init()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((500, 500))

name = get_name(screen)

start_menu(screen, all_sprites)

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
pygame.quit()