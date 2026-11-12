# my first code by the way!
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "this is a server!"}

@app.get("/itsme")
async def hello_mate():
    return {"name": "4get_it", "doing": "programming"}