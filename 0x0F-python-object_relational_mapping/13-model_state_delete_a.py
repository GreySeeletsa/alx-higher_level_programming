#!/usr/bin/python3
"""script that deletes all State objects with a name containing the letter a"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":

    # create the SQLAlchemy engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # session factory
    Session = sessionmaker(bind=engine)
    # session object
    session = Session()
    # get all states from database
    for state in session.query(State):
        # check if the state name has the letter "a"
        if "a" in state.name:
            # delete the state from session
            session.delete(state)
    # commit session to persist changes
    session.commit()
