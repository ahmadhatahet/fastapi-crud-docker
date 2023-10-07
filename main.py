from fastapi import FastAPI, HTTPException
from engine import SessionLocal
from models import Flight, Plane
import services
import uvicorn

# FastAPI application
app = FastAPI(title="CRUD using Fastapi and Docker")

# Start
@app.get("/")
def main():
    return {
        'title': 'this is an API to perform CRUD operations on MariaDB',
        'docs': 'http://localhost:5404/docs',
        'flights': 'http://localhost:5404/flights/{flight_id}'
    }


@app.get("/migrate/")
def migrate_db():
    db = SessionLocal()
    services.migrate_db(db)
    return {'message': 'Created tables and inserted sample data successfully!'}


@app.get("/flights/")
def get_all_flights():
    db = SessionLocal()
    return services.get_all_flights(db)


@app.get("/flights/{flight_id}")
def read_flight(flight_id):
    db = SessionLocal()
    flight = services.read_flight(db, flight_id)
    db.close()
    if flight is None:
        raise HTTPException(status_code=404, detail="Flight not found!")
    return flight


@app.post("/flights/")
def insert_flight(flight: Flight):
    db = SessionLocal()
    services.insert_flight(db, flight)
    db.close()
    return flight


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5400, reload=True)