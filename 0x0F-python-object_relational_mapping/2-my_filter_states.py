#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in states table
of the database hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM  states WHERE name
                LIKE BINARY '{}' ORDER BY states.id ASC""".format(sys.argv[4]))
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
