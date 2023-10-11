#!/usr/bin/env python3

import MySQLdb
import sys

def search_states(username, password, database, state_name):
    try:
        # Connecting to the MySQL server
        db = MySQLdb.connect(
            user=username,
            passwd=password,
            host='localhost',
            port=3306,
            db=database
        )
        
        # Create a cursor object to interact with the data
        cursor = db.cursor()
        
        # Use a parametized query to prevent SQL injection
        query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        
        # Fetch all rows as a list of tuples
        rows = cursor.fetchall()
        
        # Display results
        for row in rows:
            print(row)
            
        # Close the cursor and the connection
        cursor.close()
        db.close()
        
    except MySQLdb.Error as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: Python script.py <username> <password> <database> <state_name>")
    else:
        username, password, database, state_name = sys.argv[1:5]
        search_states(username, password, database, state_name)
        