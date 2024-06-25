#!/usr/bin/python3
"""
A script that creates the State "California" with the city "San Francisco"
from the database hbtn_0e_100_usa.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    stateupdate = State(name='California')
    cityupdate = City(name='San Francisco')
    stateupdate.cities.append(cityupdate)
    session.add(stateupdate)
    session.add(updatecity)
    session.commit()
    session.close()
