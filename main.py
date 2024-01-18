# pip install -r requirements.txt
import pygame       

from start_menu import get_name, start_menu
from pacmansprites import Coin, Ghost, Wall
from alert import game_win, game_over
from setup_exeption_handler import setup_handler
from filesefun import new_user

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
name = get_name(screen)
setup_handler()
new_user(name)


def main():
    all_sprites = pygame.sprite.Group()

    pacman, x, y = start_menu(screen, all_sprites)

    def is_game_over(ghost):
        return pygame.sprite.collide_mask(ghost, pacman)

    coins_i = 0
    ghost_i = 0
    wall_i = 0
    pacman_i = 1
    ghosts = []
    for sprite in all_sprites.sprites():
        if isinstance(sprite, Coin):
            coins_i += 1
        elif isinstance(sprite, Ghost):
            ghost_i += 1
            ghosts.append(sprite)
        elif isinstance(sprite, Wall):
            wall_i += 1
    pygame.mixer.music.load("data/music/fon.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0, )

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pacman.vy = -1
                    pacman.vx = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pacman.vy = 1
                    pacman.vx = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman.vy = 0
                    pacman.vx = -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pacman.vy = 0
                    pacman.vx = 1
        pygame.time.Clock().tick(24)
        screen.fill((25, 25, 25))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        if len(all_sprites.sprites()) == ghost_i + pacman_i + wall_i:
            screen.fill((25, 25, 25))
            all_sprites.update()
            all_sprites.draw(screen)
            game_win(screen, coins_i, name)
            return
        elif any(filter(is_game_over, ghosts)):
            screen.fill((25, 25, 25))
            all_sprites.update()
            all_sprites.draw(screen)
            game_over(screen, name, coins_i - (len(all_sprites.sprites()) - ghost_i - pacman_i - wall_i))
            return
    pygame.quit()


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    main()
pygame.quit()
