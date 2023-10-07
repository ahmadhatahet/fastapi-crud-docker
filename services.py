from engine import Base, engine, SessionLocal


def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()


if __name__ == "__main__":
    ...