from sqlalchemy import Column, Integer, String, DateTime
from engine import Base


# Database models
class Plane(Base):
    __tablename__ = "planes"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(100), index=True,)
    seats = Column(Integer)
    commission_date = Column(DateTime)

if __name__ == "__main__":
    ...