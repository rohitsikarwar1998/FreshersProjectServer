from datetime import datetime
from fastapi import APIRouter

from ..database import (
    retrieveDocuments,
)
from ..models.document import (
    ErrorResponseModel,
    ResponseModel,
    DocumentSchema,
)

router = APIRouter()

@router.get("/documents/",response_description="Documents retrieved")
async def getDocuments(startDate:str=datetime.today().isoformat()[0:19]):
    date=datetime.strptime(startDate, "%Y-%m-%dT%H:%M:%S")
    documents = await retrieveDocuments(date)
    if documents:
        return ResponseModel(documents, "documents data retrieved successfully")
    return ResponseModel(documents, "Empty list returned")