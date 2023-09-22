#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Main:
    """
    Args:
        mysql username
        mysql password
        database name
    """

    db_connection = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_connection)
    Session = sessionmaker(bind=engine)

    session = Session()

    my_states = session.query(State).order_by(State.id)

    for state in my_states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    Main()
