import pprint
from MapWriter import *
pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
group = pygame.sprite.Group()

gaming = True
player, level_x, level_y = generate_level(load_level('map.txt'), group)
pprint.pprint(group.sprites())
while gaming:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
    screen.fill((25, 25, 25))
    group.draw(screen)
    group.update()
    pygame.display.flip()
pygame.quit()