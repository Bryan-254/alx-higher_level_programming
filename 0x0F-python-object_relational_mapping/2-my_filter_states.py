#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute a SQL query to select all states where the name
    # matches the provided argument
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))

    # Fetch all the rows from the query result
    rows = cur.fetchall()

    # Iterate over the rows and print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
