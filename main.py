from fastapi import FastAPI, HTTPException
from engine import SessionLocal
import services
import uvicorn

# FastAPI application
app = FastAPI(title="CRUD using Fastapi and Docker")

# Start
@app.get("/")
def main():
    return {
        'title': 'this is an API to perform CRUD operations on MariaDB',
    }


# CRUD operations
@app.get("/migrate/")
def migrate_db():
    db = SessionLocal()
    services.migrate_db(db)
    return {'message': 'Created tables and inserted sample data successfully!'}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5400, reload=True)