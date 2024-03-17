#!/usr/bin/python3
"""Script for linking a Python class to a database table and fetching data."""
import sys
from model_state import Base, State

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2],
                    sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    # Create a session for interacting with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    for s in session.query(State).order_by(State.id).all():
        print(f"{s.id}: {s.name}")
