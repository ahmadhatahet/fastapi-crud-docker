from engine import Base, engine, SessionLocal
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



if __name__ == "__main__":
    ...