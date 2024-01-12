import pygame
from start_menu import *
from pacmansprites import *


pygame.init()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((700, 700))

name = get_name(screen)

pacman, x, y = start_menu(screen, all_sprites)


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pacman.vy = -7
                pacman.vx = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                pacman.vy = 7
                pacman.vx = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman.vy = 0
                pacman.vx = -7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pacman.vy = 0
                pacman.vx = 7
    pygame.time.Clock().tick(24)
    screen.fill((25, 25, 25))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()

pygame.quit()
