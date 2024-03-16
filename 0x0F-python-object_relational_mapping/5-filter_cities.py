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
    state_name = sys.argv[4]
    query = "SELECT cities.name FROM cities \
            INNER JOIN states ON states.id = cities.state_id \
           WHERE BINARY states.name = %s ORDER BY cities.id ASC;"
    cur.execute(query, (state_name, ))
    rows = cur.fetchall()
    city_names = [row[0] for row in rows]

    print(", ".join(city_names))

    cur.close()
    db.close()
