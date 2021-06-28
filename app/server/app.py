from fastapi import FastAPI
from .routes import document
app=FastAPI()


app.include_router(document.router)

@app.get("/",tags=["Root"])
async def read_root():
    return {"message":"welcome to this fantastic app!"}