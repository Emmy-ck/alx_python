#!/usr/bin/env python3

import MySQLdb
import sys


def search_states(username, password, database, state_name):
    """Connect to a MySQL server and lists all states
    where name matches the argument

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Name of database to conect to
        state_name (str): States name searched for
    """
    try:
        # Connecting to the MySQL server
        db = MySQLdb.connect(
            user=username,
            password=password,
            host='localhost',
            port=3306,
            db=database
        )
        # Create a cursor object to interact with the data
        cursor = db.cursor()

        # Excecute a safe query to display all values in states table
        # where name matches argument
        safe = ("SELECT * FROM states "
                "WHERE name LIKE BINARY %s "
                "ORDER BY id ASC")
        # Safe query using parametized query
        cursor.excecute(safe, (state_name,))
        # Fetch all rows as list if tuples
        rows = cursor.fetchall()

        # results
        for row in rows:
            print(row)
    except:
        # close the cursor and the connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: Python script.py <username> <password> <database>"
              "<state_name>")
    else:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        state_name = sys.argv[4]
        search_states(username, password,
                      database, state_name)
