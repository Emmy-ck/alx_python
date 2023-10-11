import MySQLdb
import sys


if __name__ == "__main__":
    # Check if all 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
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
        
        query = "SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC"
        cursor.execute(query)
        
        # Fetch all rows as list if tuples
        results = cursor.fetchall()
        for row in results:
            print("({}, '{}', '{}')".format(row[0], row[1], row[2]))
    except MySQLdb.Error as e:
        print("Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # close the cursor and the connection
        if db:
            db.close()