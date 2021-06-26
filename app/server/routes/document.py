from fastapi import APIRouter

from ..database import (
    retrieve_documents,
)
from ..models.document import (
    ErrorResponseModel,
    ResponseModel,
    DocumentSchema,
)

router = APIRouter()

@router.get("/",response_description="Documents retrieved")
async def get_documents():
    documents = await retrieve_documents()
    if documents:
        return ResponseModel(documents, "documents data retrieved successfully")
    return ResponseModel(documents, "Empty list returned")