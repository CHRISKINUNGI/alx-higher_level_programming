#!/usr/bin/python3
"""
This script contains the class definitionof a
State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State blueprint:
    Attributes:
    __tablename__(str): The table name
    id (int): The state id of the class
    name (str): The state name of the class
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
