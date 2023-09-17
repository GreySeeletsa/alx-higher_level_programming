#!/usr/bin/python3
"""lists all states from mySQL database"""
import sys
import MySQLdb

def list_states (username, password, database):
    """Arguments:
        mysql username
        mysql password
        mysql database
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database)
    cursor = db.cursor()

    # execute SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # fetch rows from query result
    rows = cursor.fetchall()

    # show results
    for row in rows:
        print(row)

    # close database
    db.close()

# Example usage
if __name__ == '__main__':


    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
