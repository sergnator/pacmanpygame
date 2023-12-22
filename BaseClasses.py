# исключения
class BasePacmanExceptionsGroup(Exception):
    pass


class NameTaken(BasePacmanExceptionsGroup):
    pass


# константы
class Constants:
    DataBaseOfScore = 'data/databases/score.sqlite'
    WinResult = 1
    LoseResult = 0
    Images = 'data/images/'
