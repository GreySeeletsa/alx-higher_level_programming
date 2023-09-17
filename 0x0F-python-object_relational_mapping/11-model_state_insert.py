#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database"""
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

    # create a new State object
    louisiana = State(name="Louisiana")
    # add new state
    session.add(louisiana)
    # commit session to persist changes
    session.commit()
    # print ID of recently added state
    print(louisiana.id)
