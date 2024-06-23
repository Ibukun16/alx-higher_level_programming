#!/usr/bin/python3
"""
A script that takes in arguments and displays all the values in the states
table of hbtn_0e_0_usa where name matches the argument but safe from MySQL
injections.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cusor()
    item = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name = %s
                ORDER by id ASC", (item,))
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
