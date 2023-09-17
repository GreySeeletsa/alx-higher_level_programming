#!/usr/bin/python3
"""lists all states from the hbtn_0e_0_usa database"""

import sys
import MySQLdb

if __name__ == "__main__":

    # connects to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # connect to MySQL server
    c = db.cursor()

    # retrieve all states
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")

    # fetch all rows and print states
    [print(city) for city in c.fetchall()]
