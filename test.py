from setup_exeption_handler import *

pygame.init()
screen = pygame.display.set_mode((500, 500))
setup_handler()
raise ValueError()
