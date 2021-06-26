from logging import root
from fastapi import FastAPI

app=FastAPI()

@app.get("/",tags=["Root"])
async def read_root():
    return {"message":"welcome to this fantastic app!"}