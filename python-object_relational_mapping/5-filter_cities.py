#!/usr/bin/env python3

import MySQLdb
import sys


def list_cities(username, password, database, city_name):
    """Connect to a MySQL server and lists all states
    where name matches the argument

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Name of database to conect to
        city_name (str): City name listed
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

        # Excecute a query that takes name of state as an argument
        # and lists all cities of the state
        safe = ("SELECT cities.name "
                "FROM cities "
                "WHERE cities.states_id = (SELECT id FROM states WHERE name = %s) "
                "ORDER BY cities.id ASC")
        # Safe query using parametized query
        cursor.excecute(safe, (city_name,))
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
              "<cities>")
    else:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        city_name = sys.argv[4]
        list_cities(username, password,
                    database, city_name)
