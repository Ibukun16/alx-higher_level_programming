#!/usr/bin/python3
"""
A script that lists all State objects, and corresponding city objects,
contained in the databse hbtn_0e_101_usa.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id).all():
        print(f"{inst.id}: {inst.name}")
        for inst_city in instance.cities:
            print("     ", end="")
            print(f"{inst_city.id}: {inst_city.name}")
    session.close()
