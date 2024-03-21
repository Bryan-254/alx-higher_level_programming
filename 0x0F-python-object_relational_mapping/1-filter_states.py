#!/usr/bin/python3
"""
Script that lists all states with a name starting with N
from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the results
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close cursor and database
    cur.close()
    db.close()
