#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State.name, City.id, City.name)\
        .filter(State.id == City.state_id).order_by(City.id).all()
    for c and s in instance:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.commit()
    session.close()
