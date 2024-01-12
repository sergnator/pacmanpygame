import pygame
from start_menu import *
from pacmansprites import *

pygame.init()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((700, 700))

name = get_name(screen)

start_menu(screen, all_sprites)


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.K_UP:
            vy = 10
            vx = 0
        if event.type == pygame.K_DOWN:
            vy = -10
            vx = 0
        if event.type == pygame.K_LEFT:
            vy = 0
            vx = -10
        if event.type == pygame.K_RIGHT:
            vy = 0
            vx = 10
    pygame.time.Clock().tick(10)
    screen.fill((25, 25, 25))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()

pygame.quit()
