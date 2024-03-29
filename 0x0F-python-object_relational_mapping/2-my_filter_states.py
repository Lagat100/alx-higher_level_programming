#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    cur = db.cursor()
    x = sys.argv[4]
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id;"
    cur.execute(query.format(x))
    rows = cur.fetchall()
    for row in rows:
        print(row)
