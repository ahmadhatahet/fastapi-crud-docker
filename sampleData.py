from engine import SessionLocal
from datetime import datetime
from schema import Plane, Flight

# Sample Data
def insert_sample_data(session):
    planes_data = [
        {"brand": "Boeing", "seats": 200, "commission_date": datetime(2010, 1, 1)},
        {"brand": "Airbus", "seats": 180, "commission_date": datetime(2012, 5, 15)},
    ]

    flights_data = [
        {"plane_type_id": 1, "flight_code": "BA123", "depart_location": "JFK", "destination_location": "LHR",
         "depart_time": datetime(2023, 10, 5, 10, 30), "arrival_time": datetime(2023, 10, 5, 20, 0)},
        {"plane_type_id": 2, "flight_code": "AF456", "depart_location": "CDG", "destination_location": "JFK",
         "depart_time": datetime(2023, 10, 6, 12, 0), "arrival_time": None},
    ]

    for plane_data in planes_data:
        plane = Plane(**plane_data)
        session.add(plane)

    for flight_data in flights_data:
        flight = Flight(**flight_data)
        session.add(flight)

    session.commit()
    session.close()


if __name__ == "__main__":
    # Populate sample data
    insert_sample_data(session=SessionLocal())