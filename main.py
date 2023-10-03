import uvicorn
from fastapi import FastAPI


app = FastAPI(title="CRUD using Fastapi and Docker")


@app.get("/")
def home_page():
    return {"hello": "world"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5400, reload=True)