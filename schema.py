from sqlalchemy import Column, Integer, String, DateTime
from engine import Base


# Database models
class Plane(Base):
    __tablename__ = "planes"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(100), index=True,)
    seats = Column(Integer)
    commission_date = Column(DateTime)


class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    plane_type_id = Column(Integer, index=True)
    flight_code = Column(String(10), index=True)
    depart_location = Column(String(150))
    destination_location = Column(String(150))
    depart_time = Column(DateTime)
    arrival_time = Column(DateTime, nullable=True)

if __name__ == "__main__":
    ...