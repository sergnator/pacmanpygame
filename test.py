import pygame
from MapWriter import generate_level

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
game = True
all_srites = pygame.sprite.Group()
coins = pygame.sprite.Group()
generate_level('map.txt', all_srites, coins)
clock = pygame.time.Clock()
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    clock.tick(15)
    screen.fill((0, 0, 0))
    all_srites.draw(screen)
    all_srites.update()
    pygame.display.flip()
pygame.quit()