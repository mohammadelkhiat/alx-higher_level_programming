#!/usr/bin/python3
''' prints all City objects from the database hbtn_0e_14_usa '''


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           username, password, dbname),
                           pool_pre_ping=True)

    session = Session(bind=engine)
    query = session.query(City, State)\
        .filter(City.state_id == State.id)\
        .order_by(City.id)

    for row in query:
        print("{}: ({}) {}".format(row.State.name,
                                   row.City.id,
                                   row.City.name))
    session.close()
