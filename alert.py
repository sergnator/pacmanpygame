
from start_menu import *


@add_button_back()
def game_over(screen: pygame.Surface):
    global check
    global draw
    x = 0
    clock = pygame.time.Clock()
    sound = pygame.mixer.Sound(Constants.Music + 'gameover.mp3')

    def check(event, args):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                return 'return'

    def draw(args):
        if args[3] is not None:
            sound.play()
            args[3] = None
        x = args[0]
        clock = args[1]
        width = args[2]
        font = pygame.font.Font(None, 50)
        string_render = font.render('GAME OVER', 1, pygame.Color('red'))
        rect = string_render.get_rect()
        if x < width / 2 + rect.w / 2:
            rect.x = x - rect.w
            x += 270 * clock.tick() / 1000
        else:
            rect.x = width / 2 - rect.w / 2
        rect.y = width / 2
        args[0] = x
        args[1] = clock
        screen.blit(string_render, rect)

    return [x, clock, screen.get_size()[0], sound]


@add_button_back(back_image='screen')
def game_win(screen, record, username, map):
    global check
    global draw
    res = new_record(username, map, record)
    intro = ['CONGRATULATIONS!!!', record]
    sound = pygame.mixer.Sound(Constants.Music + 'gamewin.mp3')
    if res != -1:
        intro.append('NEW RECORD!!!')

    def check(event, args):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                return 'return'

    def draw(args):
        sound = args[0]
        texts = args[1]
        width = args[2]
        font = pygame.font.Font(None, 50)
        if args[0] is not None:
            sound.play()
            args[0] = None

        for i in range(len(texts)):
            text_render = font.render(texts[i], 1, pygame.Color('yellow'))
            rect = text_render.get_rect()
            rect.x = width // 2 - rect.w // 2
            rect.y = 100 + 50 * i
            screen.blit(text_render, rect)

    return [sound, intro, screen.get_size()[0]]


def alert_of_error(error_text, screen):
    intro = ['возникала ошибка', str(error_text)]
    font = pygame.font.Font(None, 30)
    for i in range(len(intro)):
        string_render = font.render(intro[i], 1, pygame.Color('blue'))
        rect = string_render.get_rect()
        rect.x = screen.get_size()[0] // 2 - rect.w // 2
        rect.y = 100 + 30 * i
        screen.blit(string_render, rect)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
