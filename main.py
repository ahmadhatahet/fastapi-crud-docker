import uvicorn
from fastapi import FastAPI


app = FastAPI(title="CRUD using Fastapi and Docker")


@app.get("/")
def home_page():
    return {"hello": "world"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=5400, reload=True)