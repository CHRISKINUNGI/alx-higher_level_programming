#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine


class Main:
    """
    Args:
        mysql username
        mysql password
        database name
    """

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(f"mysql://{mysql_username}:{mysql_password\
            }@localhost:3306/{database_name}")

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == '__main__':
    Main()
