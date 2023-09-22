#!/usr/bin/python3
"""
    script should take 3 arguments: mysql username, mysql password and
    database name
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
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

    results = session.query(City, State).join(State)

    for city, state in results.all():
        print(f"{state.name}: ({city.id}) {city.name}")
