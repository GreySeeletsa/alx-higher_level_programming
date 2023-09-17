#!/usr/bin/python3
"""lists all states from the hbtn_0e_0_usa database"""

import sys
import MySQLdb

if __name__ == "__main__":

    # connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # return cities in the specified state
    query = ("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    c.execute(query)

    # print cities separated by commas
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
