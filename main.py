from fastapi import FastAPI, HTTPException, Depends
from models import Flight
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
def migrate_db(db = Depends(services.get_db)):
    services.migrate_db(db)
    return {'message': 'Created tables and inserted sample data successfully!'}


@app.get("/planes/")
def get_all_planes(db = Depends(services.get_db)):
    return services.get_all_planes(db)


@app.get("/flights/")
def get_all_flights(db = Depends(services.get_db)):
    return services.get_all_flights(db)


@app.get("/flights/{flight_id}")
def read_flight(flight_id, db = Depends(services.get_db)):
    flight = services.read_flight(db, flight_id)
    if flight is None:
        raise HTTPException(status_code=404, detail="Flight not found!")
    db.close()
    return flight


@app.post("/flights/")
def insert_flight(flight: Flight, db = Depends(services.get_db)):
    flight = services.insert_flight(db, flight)
    db.close()
    return flight


@app.delete("/flights/{flight_id}")
def delete_flight(flight_id: int, db = Depends(services.get_db)):
    flight = services.read_flight(db, flight_id)
    if flight is None:
        db.close()
        raise HTTPException(status_code=404, detail="Flight not found!")
    db.delete(flight)
    db.commit()
    db.close()
    return {"message": "Flight deleted successfully"}


@app.put("/flights/{flight_id}")
def update_flight(flight_id: int, flight: Flight, db = Depends(services.get_db)):
    db_flight = services.read_flight(db, flight_id)
    if db_flight is None:
        db.close()
        raise HTTPException(status_code=404, detail="Flight not found!")
    for var, value in flight.model_dump(exclude_none=True).items():
        setattr(db_flight, var, value)
    db.commit()
    db.refresh(db_flight)
    db.close()
    return db_flight


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=5400, reload=True)