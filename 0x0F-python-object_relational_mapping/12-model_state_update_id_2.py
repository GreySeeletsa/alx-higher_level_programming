#!/usr/bin/python3
"""script that changes the name of State object"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":

    # create SQLAlchemy engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # session factory
    Session = sessionmaker(bind=engine)
    # session object
    session = Session()

    # Get the state with ID 2 from database
    state = session.query(State).filter_by(id=2).first()
    # update name of the state
    state.name = "New Mexico"
    # commit session to persist changes
    session.commit()
