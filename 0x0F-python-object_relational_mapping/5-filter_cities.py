#!/usr/bin/python3
''' a script that takes in the name of a state as an argument
and lists all cities of that state
using the database hbtn_0e_4_usa '''


import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    if ';' in sys.argv[4]:
        statename = sys.argv[4].split(';')[0].strip("'\"")
    else:
        statename = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=dbname, charset="utf8")
    cur = conn.cursor()
    cur.execute("\
                SELECT cities.name\
                FROM cities LEFT JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = '{}'\
                ORDER BY cities.id\
                ".format(statename))
    query_rows = cur.fetchall()
    result = []
    for row in query_rows:
        result.append(row[0])
    separator = ', '
    print(separator.join(result))
    cur.close()
    conn.close()
