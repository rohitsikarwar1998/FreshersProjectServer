import motor.motor_asyncio
from datetime import datetime


MONGO_DETAILS="mongodb://localhost:27017"

client=motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# freshers_project is database name
database=client.freshers_project

documentCollection=database.get_collection("documents")

def documentHelper(document)->dict:
    return {
        "id":str(document["_id"]),
        "title":document["title"],
        "date":document["date"],
        "link":document["link"],
    }

async def retrieveDocuments(startDate:datetime):
    documents=[]
    async for document in documentCollection.find({"date":{"$lt":startDate}}).limit(16):
        documents.append(documentHelper(document))
    return documents