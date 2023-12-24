import sqlite3
from BaseClasses import *


def new_user(username):
    """создание нового пользователя"""
    con = sqlite3.connect(Constants.DataBaseOfScore)
    cur = con.cursor()
    req = f"insert into score(name, max_time, map_of_max_time) values('{username}', 'unknown', 'unknown')"
    ex = False
    try:
        cur.execute(req)
    except sqlite3.IntegrityError:
        ex = True
    if ex:
        raise NameTaken('имя занято')
    con.commit()
    con.close()


def new_record(username, name_map, record):
    """изменение рекорда"""
    con = sqlite3.connect(Constants.DataBaseOfScore)
    cur = con.cursor()
    req = f"update score\nset max_time = '{record}',\nmap_of_max_time = '{name_map}'\nwhere name = '{username}'"
    cur.execute(req)
    con.commit()
    con.close()


def get_users():
    """получение всех юзеров"""
    con = sqlite3.connect(Constants.DataBaseOfScore)
    cur = con.cursor()
    req = f"select * from score"
    users = cur.execute(req).fetchall()
    con.close()
    return users


