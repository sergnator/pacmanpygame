import sqlite3
import Constants
import os


def new_user(username):
    """создание нового пользователя"""
    con = sqlite3.connect(Constants.DataBaseOfScore)
    cur = con.cursor()
    users = get_users()
    for user in users:
        if username == user[Constants.name_key]:
            con.close()
            return
    req = f"insert into score(name, max_score) values('{username}', 0)"
    cur.execute(req)
    con.commit()
    con.close()


def new_record(username, record):
    """изменение рекорда"""
    users = get_users()
    for el in users:
        if el[Constants.name_key] == username:
            if int(el[Constants.record_time_key]) >= int(record):
                return -1
            else:
                break
    req = f"update score\nset max_score = '{record}'\nwhere name = '{username}'"
    con = sqlite3.connect(Constants.DataBaseOfScore)
    cur = con.cursor()
    cur.execute(req)
    con.commit()
    con.close()


def get_users():
    """получение всех юзеров"""
    con = sqlite3.connect(Constants.DataBaseOfScore)
    cur = con.cursor()
    req = f"select * from score"
    users = cur.execute(req).fetchall()  # [(id, name, record_score), ...]
    con.close()
    return users


def get_maps():
    """названия всех карт"""
    all_maps = list(map(lambda x: x[:-4], os.listdir(Constants.Maps)))
    return all_maps
