import sqlite3
import json


def sql2json(database, table, json_file):
    try:
        if database[-3:] != ".db":
            db = sqlite3.connect(database + ".db")
        else:
            db = sqlite3.connect(database)
    except:
        raise sqlite3.DatabaseError

    cur = db.cursor()
    cur.execute("SELECT * FROM " + table)

    input1 = cur.fetchall()
    output = dict()
    for i in input1:
        output[i[0]] = {"name": i[1], "description": i[2], "hotkey": i[3], "xp": i[4], "base_cost": i[5],
                        "category": i[6]}

    with open(json_file, 'w') as fp:
        json.dump(output, fp)