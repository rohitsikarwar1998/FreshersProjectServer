from datetime import datetime
from pydantic import BaseModel,Field

class DocumentSchema(BaseModel):
    title:str=Field(...)
    date:datetime=Field(...)
    link:str=Field(...)
    num:int=Field(...)


def ResponseModel(data,message):
    return {
        "data":[data],
        "code":200,
        "message":message,
    }

def ErrorResponseModel(error,code,message):
    return {"error":error,"code":code,"message":message}