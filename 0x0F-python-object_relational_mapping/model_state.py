#!/usr/bin/python3
"""
    python file that contains the class definition of a
    State and an instance Base = declarative_base()
"""
from sqlalchemy import create_engine


class State(Base):
    """
        args
    """

    __tablename__ =  'states'

    id=column(Integer, primary_key=True, )
    name=column(String(128), Null=False) 
