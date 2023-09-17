#!/usr/bin/python3
"""prints all City objects from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":

    # create the SQLAlchemy engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # session factory
    Session = sessionmaker(bind=engine)
    # session object
    session = Session()
    # get cities and their associated states
    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        # print results
        print("{}: ({}) {}".format(state.name, city.id, city.name))
