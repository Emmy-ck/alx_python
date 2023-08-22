#!/usr/bin/env python3

import MySQLdb
import sys


def searched_states(username, password, database, state_search):
    """Connect to a MySQL server and lists all states in ascending order

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Name of database to conect to
        state_search (str): States name searched for
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

        # Excecute the SQL query to display all values in states table where name matches
        cursor.execute("SELECT * FROM states"
                       "WHERE BINARY name = '{}'"
                       "ORDER BY states.id ASC").format(state_search)

        # Fetch all rows as list if tuples
        rows = cursor.fetchall()

        # results
        for row in rows:
            print(row)
    except:
        # close the cursor connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: Python script.py <username> <password> <database> <state_search>")
    else:
        username, password, database, state_search = sys.argv[1], sys.argv[2], sys.argv[3], sys.arg[4]
        searched_states(username, password, database, state_search)
