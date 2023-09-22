#!/usr/bin/python3
"""
    script that prints the first State object from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_connnection = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])

    engine = create_engine(db_connnection)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id).first()

    if states is None:
        print("Nothing")

    else:
        print(f"{states.id}: {states.name}")
