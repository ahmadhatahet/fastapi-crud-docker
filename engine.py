from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os


# load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ModuleNotFoundError as e:
    pass # in docker environment variables are automatically loaded

# database connection
DATABASE_URL = f"mariadb+mariadbconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(DATABASE_URL)

# base class
Base = declarative_base()

# create session to interact
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


if __name__ == "__main__":
    ...