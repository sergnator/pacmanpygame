# исключения
class BasePacmanExceptionsGroup(Exception):
    pass


class NameTaken(BasePacmanExceptionsGroup):
    pass


# константы
class Constants:
    DataBaseOfScore = 'data/databases/score.sqlite'
    Maps = 'data/maps/'
    WinResult = 1
    LoseResult = 0
    Images = 'data/images/'
    id_key = 0
    name_key = 1
    record_time_key = 2
    record_map_key = 3
