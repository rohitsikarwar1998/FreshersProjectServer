from fastapi import FastAPI
app=FastAPI()
from .routes import document


app.include_router(document.router)

@app.get("/",tags=["Root"])
async def read_root():
    return {"message":"welcome to this fantastic app!"}