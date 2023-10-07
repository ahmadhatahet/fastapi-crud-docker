from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PlaneBase(BaseModel):
    brand: str
    seats: int
    commission_date: datetime

class FlightBase(BaseModel):
    plane_type_id: int
    flight_code: str
    depart_location: str
    destination_location: str
    depart_time: datetime
    arrival_time: Optional[datetime] = None

class Plane(PlaneBase):
    id: int

    class Config:
        from_attributes = True

class Flight(FlightBase):
    id: int

    class Config:
        from_attributes = True

if __name__ == "__main__":
    ...