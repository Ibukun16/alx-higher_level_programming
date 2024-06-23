#!/usr/bin/python3
"""
A script that lists all states from the hbtn_0e_0_usa database.

This script takes 3 arguments, uses the MySQLdb module,
and connect to MySQL server.
Result from the script sorted in ascending order by states.id.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close
