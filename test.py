import pygame.time
from ghostsprite import *
from test2 import *
pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
group = pygame.sprite.Group()

gaming = True
a = Ghost(250, 50, group)
clock = pygame.time.Clock()
while gaming:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                a.vx = 10
                a.vy = 0
    clock.tick(14)
    screen.fill((0, 0, 0))
    group.draw(screen)
    group.update()
    pygame.display.flip()
    if a.rect.x >= 468:
        a.vx = -10
    elif a.rect.x <= 0:
        a.vx = 10
    if a.rect.y <= 0:
        a.vy = 10
    elif a.rect.y >= 468:
        a.vy = -10
pygame.quit()
