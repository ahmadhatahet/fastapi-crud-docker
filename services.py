from engine import Base, engine, SessionLocal
import schema
import models
from sampleData import insert_sample_data


def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

def migrate_db(db):
    # ceate tables
    create_tables()
    # insert sample data
    insert_sample_data(db)


def get_all_flights(db):
    flights = db.query(schema.Flight).all()
    return list(map( models.Flight.model_validate, flights))


def read_flight(db, flight_id):
    flight = db.query(schema.Flight).filter(schema.Flight.id == flight_id).first()
    return flight


def insert_flight(db, flight):
    db_flight = schema.Flight()
    for var, value in flight.model_dump(exclude_none=True).items():
        setattr(db_flight, var, value)
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return flight


if __name__ == "__main__":
    ...