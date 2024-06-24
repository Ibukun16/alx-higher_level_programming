#!/usr/bin/python3
"""
A python file that contains class definition of a State and an instance
Base as an instance of declarative_base().
"""
from sqalchemy import Column, Integer, String, MetaData
from sqalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """A class with id and name attributes of each state"""

    __tablename__ = 'states'
    id = Colum(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
