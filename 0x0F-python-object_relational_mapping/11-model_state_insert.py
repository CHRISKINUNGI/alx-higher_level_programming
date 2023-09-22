#!/usr/bin/python3
"""
    script that adds the State object “Louisiana” to the database
    hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
        args:
            mysql username -argv[1]
            mysql password -argv[2]
            database name -argv[3]
    """

    db_connection = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])

    engine = create_engine(db_connection)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="Louisiana")
    session.add(state)
    session.commmit()

    print(f"{state.id}")
    session.close()
