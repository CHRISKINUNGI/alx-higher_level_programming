#!/usr/bin/python3
"""
    python file that contains the class definition of a
    State and an instance Base = declarative_base()
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

""" creating engine """
engine = create_engine("mysql://root:Kitchen2020.@localhost:3306")


""" Base  declaration """
Base = declarative_base()


class State(Base):
    """
        args:
             id
             name
    """

    __tablename__ = 'states'

    id = column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = column(String(128), nullable=False)


""" Migration of the data """
Base.metadata.create_all(engine)


""" creating Session """
Session = sessionmaker(bind=engine)
session = Session()
