import sqlite3 as lite
import sys
import os

con = None

try:
    # path = os.path.dirname(__file__) + "\\db.sqlite3"
    # print(path)
    path = "F:\\NetworkProject\\Network\\db.sqlite3"
    con = lite.connect(path)

    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()

    print("SQLite version: %s" % data)

except lite.Error as e:

    print("Error %s:" % e.args[0])
    sys.exit(1)

finally:

    if con:
        con.close()