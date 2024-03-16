#!/usr/bin/python3
import MySQLdb
import sys


def search_states_by_name(username, password, database, state_name):
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database)

    cur = db.cursor()
    sql_query = "SELECT * FROM states\
            WHERE name = '{}' ORDER BY id ASC;".format(state_name)
    cur.execute(sql_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
