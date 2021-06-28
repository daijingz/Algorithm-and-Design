import sqlite3
from sqlite3 import Error
import json


#def sql2json(database, table, json_file):
#    try:
#        if database[-3:] != ".db":
#            db = sqlite3.connect(database + ".db")
#        else:
#            db = sqlite3.connect(database)
#    except:
#        raise sqlite3.DatabaseError
#
#    cur = db.cursor()
#    cur.execute("SELECT * FROM " + table)
#
#    input1 = cur.fetchall()
#    output = dict()
#    for i in input1:
#        output[i[0]] = {"name": i[1], "description": i[2], "hotkey": i[3], "xp": i[4], "base_cost": i[5],
#                        "category": i[6]}
#
#    with open(json_file, 'w') as fp:
#        json.dump(output, fp)


def SQL_Connection():
    try:
        con = sqlite3.connect(':memory:')
        print("Connection is established: Database is created in memory")
        con.close()
    except Error:
        print(Error)
        raise Exception()
    finally:
        print("This function has been successfully finished")