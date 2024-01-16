from alert import *
from BaseClasses import BasePacmanExceptionsGroup


def setup_handler():
    '''Устанавливает обработчик'''
    sys.excepthook = handler


def handler(exc_type, exc_value, exc_traceback):
    '''Обработчик исключений, если ошибка 'не фатальна', то выводится на экран,
     если не обрабатываемая, то просто принтится в консоль'''
    if issubclass(exc_type, BasePacmanExceptionsGroup):
        alert_of_error(exc_value, pygame.display.set_mode((500, 500)))
    else:
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
