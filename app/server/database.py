import motor.motor_asyncio


MONGO_DETAILS="mongodb://localhost:27017"

client=motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database=client.documents

document_collection=database.get_collection("documents_collection")

def document_helper(document)->dict:
    return {
        "id":str(document["_id"]),
        "title":document["title"],
        "date":document["date"],
        "link":document["link"],
    }

async def retrieve_documents():
    documents=[]
    async for document in document_collection.find():
        documents.append(document_helper(document))
    return documents