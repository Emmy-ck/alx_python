"""
Lists State objects that with letter 'a' from database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
        
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306
    
    # Create a connection to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:{port}/{database}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and display State objects with letter 'a' sorted by states.id
    states = session.query(State).filter(State.name.like('%a%')).order_by
    (State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
