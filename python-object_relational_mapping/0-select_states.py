#!/usr/bin/env python3

import MySQLdb
import sys


def list_states(username, password, database):
    """Connect to a MySQL server and lists all states in ascending order

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Name of database to conect to
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

        # Excecute the SQL query to get states sorted by states
        cursor.execute("SELECT * FROM states ORDER BY states.id")

        # Fetch all rows as list if tuples
        rows = cursor.fetchall()

        # reaults
        for row in rows:
            print(row)
    except:
        # close the cursor connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: Python script.py <username> <password> <database>")
    else:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        list_states(username, password, database)
