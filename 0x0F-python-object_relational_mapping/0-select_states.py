#!/usr/bin/python3

"""Lists all states from the database hbtn_0c_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], port=3306, db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    conn.close()
