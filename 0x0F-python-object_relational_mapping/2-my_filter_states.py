#!/usr/bin/python3

"""lists all states from hbtn_0e_0_usa database."""

import sys
import MySQLdb

if __name__ == "__main__":

    # connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # return states with the specified name
    c.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))

    # fetch all rows and print states
    [print(state) for state in c.fetchall()]
