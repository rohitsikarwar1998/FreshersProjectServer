import motor.motor_asyncio


MONGO_DETAILS="mongodb://localhost:27017"

client=motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database=client.freshers_project

documentCollection=database.get_collection("documents")

def documentHelper(document)->dict:
    return {
        "id":str(document["_id"]),
        "title":document["title"],
        "date":document["date"],
        "link":document["link"],
    }

async def retrieveDocuments():
    documents=[]
    async for document in documentCollection.find():
        documents.append(documentHelper(document))
    return documents