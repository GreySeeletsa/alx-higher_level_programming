#!/usr/bin/python3
"""lists all states from the hbtn_0e_0_usa database."""
import sys
import MySQLdb

if __name__ == "__main__":
    import MySQLdb
    import sys

    # retieve command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # cursor object to execute queries
    cursor = db.cursor()

    # have placeholders
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # execute query with state name as a parameter
    cursor.execute(sql_query, (state_name,))

    # fetch all rows returned by query
    rows = cursor.fetchall()

    # print results
    for row in rows:
        print(row)

    # Close database connection
    cursor.close()
    db.close()
