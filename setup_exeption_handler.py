
from alert import *


def setup_handler():
    sys.excepthook = handler


def handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, BasePacmanExceptionsGroup):
        alert_of_error(exc_value, pygame.display.set_mode((500, 500)))
    else:
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
