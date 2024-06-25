#!/usr/bin/python3
"""
A file that contains State class and Base as an instance of declarative_base
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

rmetadata = MetaData()
Base = declarative_base(metadata=rmetadata)


class State(Base):
    """
    Class definition with id and name attributes of each state
    """
    __tablename__ = 'state'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states)
