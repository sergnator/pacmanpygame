from pacmansprite import *
pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
group = pygame.sprite.Group()

gaming = True
a = Ghost(250, 50, group)
b = Pacman(250, 100, group)
b.vx = 10
clock = pygame.time.Clock()
while gaming:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                a.vx = 10
                a.vy = 0
    clock.tick(24)
    screen.fill((25, 25, 25))
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
    if b.rect.x >= 468:
        b.vx = -10
    elif b.rect.x <= 0:
        b.vx = 10
    if b.rect.y <= 0:
        b.vy = 10
    elif b.rect.y >= 468:
        b.vy = -10
pygame.quit()
