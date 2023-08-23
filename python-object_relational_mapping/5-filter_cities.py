import MySQLdb
import sys


def list_cities(username, password, database, state_name):
    """Connect to a MySQL server and lists all states
    where name matches the argument

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Name of database to conect to
        state_name (str): Name of state
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

        # Execute query that lists all cities from the states in the db
        query = ("SELECT cities.id, cities.name, states.name "
                 "FROM cities INnER JOIN states"
                 "ON cities.state_id = states.id "
                 "WHERE BiNARY states.name = '{}' "
                 "ORDER BY cities.id ASC")
        # Execute the query with parameter
        cursor.execute = (query, (state_name,))
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
        print("Usage: Python script.py <username> <password> <database> "
              "<state_name>")
    else:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        state_name = sys.argv[4]
        list_cities(username, password, database,
                    state_name)
