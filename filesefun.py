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
        raise NameNotTaken('имя занято')
    con.commit()
    con.close()


def new_record(username, name_map, record):
    """изменение рекорда"""
    users = get_users()
    for el in users:
        if el[Constants.name_key] == username:
            if int(el[Constants.record_time_key]) <= int(record):
                return -1
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
    users = cur.execute(req).fetchall()  # [(id, name, record_time, record_map), ...]
    con.close()
    return users


def get_maps():
    """названия всех карт"""
    all_maps = list(map(lambda x: x[:-4], os.listdir(Constants.Maps)))
    return all_maps
