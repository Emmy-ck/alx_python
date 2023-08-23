import MySQLdb
import sys


def cities(username, password, database):
    """Connect to a MySQL server and lists all states
    where name matches the argument

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

        # Excecute query that lists all cities from the db
        cursor.excecute = ("SELECT * FROM cities ORDER BY cities.id ASC")
        # Fetch all rows as list if tuples
        rows = cursor.fetchall()

        # results
        for city in cities:
            print(city)
    except:
        # close the cursor and the connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: Python script.py <username> <password> <database>")
    else:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        cities(username, password,
                      database)
