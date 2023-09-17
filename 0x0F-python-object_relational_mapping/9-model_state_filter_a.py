#!/usr/bin/python3
"""script that lists all State objects that contain letter a"""
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

    # database and print its ID and name
    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))