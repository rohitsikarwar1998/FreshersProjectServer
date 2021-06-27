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

@router.get("/",response_description="Documents retrieved")
async def getDocuments():
    documents = await retrieveDocuments()
    if documents:
        return ResponseModel(documents, "documents data retrieved successfully")
    return ResponseModel(documents, "Empty list returned")