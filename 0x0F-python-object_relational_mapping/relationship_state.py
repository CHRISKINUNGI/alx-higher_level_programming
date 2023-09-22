#!/usr/bin/python3
"""
This script contains the class definition of a State
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship


class State(Base):
    """
    State class with a relationship to City objects
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name


relationship(State, backref="state", cascade="all, delete-orphan")
